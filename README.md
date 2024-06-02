# eCommerce Microservices

## Introduction

This project is an eCommerce platform built using microservices architecture. It consists of two main components: the API server and the client server. The API server handles backend operations such as processing purchases and managing inventory, while the client server provides a user interface for customers to browse products and make purchases.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Installation

To get started with the eCommerce microservices project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/eilaytal/ecommerce-microservices.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ecommerce-microservices
   ```

3. Install dependencies for both the API server and the client server:
   ```bash
   cd api_server
   pip install -r requirements.txt
   cd ../client_server
   pip install -r requirements.txt
   ```

## Usage

To run the eCommerce microservices project, follow these steps:

1. Start the API server:
   ```bash
   cd api_server
   python api_server.py
   ```

2. Start the client server:
   ```bash
   cd ../client_server
   python client_server.py
   ```

3. Access the client server in your web browser:
   ```
   http://localhost:5001
   ```

## Directory Structure

```
ecommerce-microservices/
│
├── api_server/                   # API server component
│   ├── api_server.py             # Main API server application
│   ├── Dockerfile                # Dockerfile for API server
│   └── requirements.txt          # Python dependencies
│
├── client_server/                # Client server component
│   ├── client_server.py          # Main client server application
│   ├── Dockerfile                # Dockerfile for client server
│   ├── requirements.txt          # Python dependencies
│   └── templates/                # HTML templates
│       └── index.html            # Main HTML template
│
├── .gitignore                    # Git ignore file
├── docker-compose.yml            # Docker Compose configuration
└── README.md                     # Project README file
```

## Technologies Used

- Python: Programming language used for backend development.
- Flask: Web framework used for building the API server.
- MongoDB: NoSQL database used for storing purchase data.
- Kafka: Message broker used for handling purchase events.
- HTML/CSS: Frontend technologies used for building the client server.
- Docker: Containerization technology used for packaging and deploying the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.
