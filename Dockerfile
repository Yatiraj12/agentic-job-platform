# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app
COPY run.py .

# Start FastAPI using Render port
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]