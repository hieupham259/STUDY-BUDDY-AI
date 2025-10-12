## Base image
FROM python:3.11-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copy requirements.txt first to leverage Docker layer caching
COPY requirements.txt .

## Install python dependencies (this layer will be cached if requirements.txt doesn't change)
RUN pip install --no-cache-dir -r requirements.txt

## Copy the rest of the application files
COPY . .

# Used PORTS
EXPOSE 8501

# Run the app 
CMD ["streamlit", "run", "application.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]