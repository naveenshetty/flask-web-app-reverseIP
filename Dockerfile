# Use a Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt /app/

# Install the dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app/

# Expose port 5000 for the Flask app to be accessible
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "main.py"]
