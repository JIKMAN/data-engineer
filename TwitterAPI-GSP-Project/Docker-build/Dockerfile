# Use an official Python runtime as a parent image
FROM python:3.9.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the contatiner at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/jungik-ta-aa9fa3a5da97.json"

# Run app.py when the container launches
CMD ["python", "tweet.py"]