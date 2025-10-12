#!/bin/bash
echo "Building Study Buddy AI Docker image..."
docker build -t study-buddy-ai .

echo
echo "Starting Study Buddy AI container..."
docker run --name study-buddy -d -p 8501:8501 study-buddy-ai

echo
echo "Container started! Access the app at: http://localhost:8501"
echo "To stop the container, run: docker stop study-buddy"
echo "To remove the container, run: docker rm study-buddy"