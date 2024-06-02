# Dockerfile for Client Server
FROM python:3.10.13-alpine

# Set the working directory
WORKDIR /client_server

# Copy the current directory contents into the container at /client_server
COPY . /client_server

# Install dependencies
RUN apk add --no-cache \
    build-base \
    openssl-dev \
    lz4-dev \
    musl-dev \
    librdkafka-dev
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run client_server.py when the container launches
CMD ["python", "client_server.py"]
