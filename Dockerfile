# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the local contents into the container at /app
COPY . /app

# Install Flask and other required packages
RUN pip install --no-cache-dir Flask

# Set the environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Specify the port number the container should expose
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
