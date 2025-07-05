# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire app code
COPY . .

# Expose the port (if you're using Flask or similar)
EXPOSE 5000

# Run your main app
CMD ["python", "run.py"]
