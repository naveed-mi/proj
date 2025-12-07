# SimpleTimeService (Task 1 – Application & Docker)

SimpleTimeService is a lightweight Python microservice that returns the current
timestamp and the caller’s IP address in JSON format. It is containerized
following security and best-practice guidelines, and is intended for deployment
on AWS ECS/EKS or any container runtime.

## Features
- Minimal Python HTTP server (no external dependencies)
- Returns JSON with timestamp + client IP
- Dockerized using a non-root user
- Small image size (python:3.11-slim)

## Project Structure
app/
├── app.py
├── Dockerfile
└── .dockerignore

## Run Locally
python3 app.py

## Test
curl http://localhost:8080/

## Build Docker Image
docker build -t simple-time-service .

## Run Container
docker run --rm -p 8080:8080 simple-time-service

## Test
curl http://localhost:8080/


## Testing Output Example
{
  "timestamp": "2025-12-07T18:25:43.511Z",
  "ip": "127.0.0.1"
}

## Security
- Runs as non-root user `appuser`
- Follow the best practices for Docker


