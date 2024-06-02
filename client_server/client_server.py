from flask import Flask, request, redirect, render_template, jsonify
from confluent_kafka import Producer
import json
import requests
import os

app = Flask(__name__)

# Set up Kafka producer with confluent-kafka
producer = Producer({
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
})

def acked(err, msg):
    """Callback function for Kafka message delivery reports."""
    if err is not None:
        print(f"Failed to deliver message: {str(msg)}: {str(err)}")
    else:
        print(f"Message produced: {str(msg)}")

@app.route('/')
def index():
    """Render the main HTML form for buying an item."""
    return render_template('index.html')

@app.route('/buyItem', methods=['POST'])
def buy_item():
    """Handle the item purchase request."""
    try:
        # Collect item details from the form
        item = {
            "user_id": request.form['user_id'],
            "item_name": request.form['item_name']
        }
        # Produce the item to Kafka
        producer.produce('item_purchases', json.dumps(item).encode('utf-8'), callback=acked)
        producer.poll(0)  # Trigger callback execution
        return redirect('/')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/viewPurchases', methods=['POST'])
def get_all_bought_items():
    """Handle the request to view all purchased items."""
    try:
        user_id = request.form['user_id']
        # Call the API server to get all purchased items
        api_server_url = os.getenv('API_SERVER_URL', 'http://localhost:5002')
        response = requests.post(f'{api_server_url}/getAllBoughtItems', json={'user_id': user_id})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5001 in debug mode
    app.run(debug=True, host='0.0.0.0', port=5001)
