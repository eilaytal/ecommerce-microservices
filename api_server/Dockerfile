# Dockerfile for API Server
FROM python:3.10.13-alpine

# Set the working directory
WORKDIR /api_server

# Copy the current directory contents into the container at /api_server
COPY . /api_server

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run api_server.py when the container launches
CMD ["python", "api_server.py"]
