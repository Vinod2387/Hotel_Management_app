# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files into container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
