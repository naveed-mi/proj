# SimpleTimeService (Task 1 – Application & Docker)

SimpleTimeService is a lightweight Python microservice that returns the current
timestamp and the caller’s IP address in JSON format. It is containerized
following security and best-practice guidelines, and is intended for deployment
on AWS ECS/EKS or any container runtime.

---

## 📌 Features

- Minimal Python HTTP server (no external dependencies)
- Returns JSON:
  ```json
  {
    "timestamp": "<current ISO8601 UTC time>",
    "ip": "<client ip>"
  }
Detects client IP via:

X-Forwarded-For header (if behind load balancer)

Direct socket IP (fallback)

Dockerized using non-root user

Small image (python:3.11-slim)

Ideal for DevOps / Terraform / AWS testing

📁 Project Structure
Copy code
app/
├── app.py
├── Dockerfile
└── .dockerignore
🚀 Run Locally (Without Docker)
bash
Copy code
python3 app.py
Test it:

bash
Copy code
curl http://localhost:8080/
🐳 Build the Docker Image
From the app/ directory:

bash
Copy code
docker build -t simple-time-service .
Or tag for Docker Hub:

bash
Copy code
docker build -t <dockerhub-username>/simple-time-service:latest .
🏃 Run the Container
bash
Copy code
docker run --rm -p 8080:8080 simple-time-service
Or using your Docker Hub tag:

bash
Copy code
docker run --rm -p 8080:8080 <dockerhub-username>/simple-time-service:latest
🧪 Testing the Service
bash
Copy code
curl http://localhost:8080/
Expected response:

json
Copy code
{
  "timestamp": "2025-12-07T18:25:43.511Z",
  "ip": "127.0.0.1"
}
