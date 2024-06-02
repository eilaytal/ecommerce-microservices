from flask import Flask, request, jsonify
from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['purchase_db']
collection = db['purchases']

# Kafka Consumer setup
kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
consumer = Consumer({
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': 'purchase_group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['purchases'])

@app.route('/buy', methods=['POST'])
def buy_item():
    """Endpoint to handle the purchase of an item."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        return jsonify({"message": "Purchase request sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getAllBoughtItems', methods=['GET'])
def get_all_bought_items():
    """Endpoint to retrieve all purchased items."""
    try:
        purchased_items = list(collection.find({}, {'_id': 0}))
        return jsonify(purchased_items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def consume_messages():
    """Function to consume messages from Kafka and store them in MongoDB."""
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        data = json.loads(msg.value().decode('utf-8'))
        collection.insert_one(data)

if __name__ == '__main__':
    # Start Kafka consumer thread
    from threading import Thread
    consumer_thread = Thread(target=consume_messages)
    consumer_thread.start()
    
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
