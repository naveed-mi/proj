# DevOps Challenge – Infrastructure & Container Deployment

This repository contains my implementation of a DevOps assessment focused on
building a containerized microservice and deploying it onto AWS using
production-grade Infrastructure as Code (IaC).

The solution demonstrates:
- Secure containerization (non-root user, small image)
- Highly available AWS architecture using Terraform
- ECS Fargate service running in private subnets
- Application Load Balancer (public) routing traffic to the service
- Clean repository layout following best practices

---

## 📁 Repository Structure

```
.
├── app/         # Containerized microservice (Dockerfile + Python app)
└── terraform/   # Terraform code to deploy AWS infrastructure
```

Each component operates independently and can be tested or deployed separately.

---

## 🚀 Application (app/)

Located in `/app`, this folder contains a lightweight Python HTTP service that returns:

{
  "timestamp": "<current_time>",
  "ip": "<client_ip>"
}

It includes:

- app.py — minimal web server
- Dockerfile — runs as non-root, optimized for size
- .dockerignore — excludes unnecessary files
- README with build/run instructions

Build and run locally:

```
docker build -t simple-time-service ./app
docker run --rm -p 8080:8080 simple-time-service
```

---

## ☁️ Infrastructure (terraform/)

Located in `/terraform`, this folder contains the Terraform code that deploys:

- VPC (2 public + 2 private subnets)
- ECS Fargate cluster
- ECS service running in private subnets
- Application Load Balancer (public)
- CloudWatch log group
- IAM roles for ECS
- Route tables, IGW, NAT gateway

### Deployment Steps

```
cd terraform
terraform init
terraform plan
terraform apply
```

Set the container image to deploy in `terraform.tfvars`:

```
container_image = "your-dockerhub-username/simple-time-service:latest"
```

Retrieve the ALB endpoint:

```
terraform output -raw alb_dns_name
```

Test:

```
curl http://<alb_dns_name>/
```

---

## 🔐 Security Practices

- No credentials included in the repository
- Containers run as a non-root user
- Private subnets for compute workloads
- Public exposure only via ALB

---

## ⭐ Extra Enhancements (Optional)

This project is prepared to support:

### ✔ Remote Terraform backend  
Using S3 + DynamoDB state locking (backend.tf)
