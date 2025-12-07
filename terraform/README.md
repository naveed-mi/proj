# Terraform Infrastructure (Task 2)

This folder contains Terraform code to deploy a containerized service onto AWS using ECS Fargate, VPC networking, and an Application Load Balancer (ALB). This task is independent of Task 1 and supports deploying any container image of your choice.

---

## 🚀 Overview

Terraform provisions the following:

### 🔹 Networking
- VPC 
- 2× Public Subnets
- 2× Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables + Associations

### 🔹 Compute (ECS Fargate)
- ECS Cluster
- ECS Task Definition
- ECS Service running in **private** subnets

### 🔹 Load Balancer
- Application Load Balancer in public subnets
- Listener (HTTP :80)
- Target Group for ECS tasks

### 🔹 IAM
- ECS Task Execution Role
- ECS Task Role

### 🔹 Logging
- CloudWatch Log Group

---

## 📁 Folder Structure

```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
└── README.md   ← this file
```

---

## 🛠 Prerequisites

### ✔ Terraform v1.5+
Install from: https://developer.hashicorp.com/terraform

### ✔ AWS Credentials (DO NOT commit them)
Authenticate using one option below:

#### Option A — Environment Variables
```
export AWS_ACCESS_KEY_ID="xxxx"
export AWS_SECRET_ACCESS_KEY="xxxx"
export AWS_DEFAULT_REGION="eu-west-1"
```

#### Option B — AWS CLI Profile
```
aws configure --profile myprofile
export AWS_PROFILE=myprofile
```

#### Option C — AWS SSO
If SSO is enabled, Terraform uses it automatically.

---

## 🔧 Configuration Required

Before running Terraform, update:

### `terraform.tfvars`
```
container_image = "your-dockerhub-username/simple-time-service:latest"
```

This tells ECS which container to deploy.

---

## ▶️ Deployment Commands

### 1. Initialize providers
```
terraform init
```

### 2. Plan infrastructure
```
terraform plan
```

### 3. Apply changes
```
terraform apply
```

Approve with `yes`.

---

## 🌍 Test the Deployment

Get the ALB DNS name:
```
terraform output -raw alb_dns_name
```

Test the service:
```
curl http://<alb_dns_name>/
```

---

## 🧹 Destroy the Infrastructure

```
terraform destroy
```

---


- Centralized Terraform state
- DynamoDB state locking
- No local `.tfstate` files

---

## 2️⃣ CI/CD (GitHub Actions)

Add `.github/workflows/ci-cd.yml`  
Pipeline will:
- Build Docker image  
- Push to registry  
- Run Terraform plan/apply  
- Use GitHub Secrets for AWS + Docker credentials  


---

## ✔ Requirement Validation

| Required Item | Status |
|---------------|--------|
| VPC (public + private) | ✅ |
| ECS or EKS | ✅ ECS Fargate |
| Service in private subnets | ✅ |
| Public ALB fronting service | ✅ |
| terraform plan/apply only | ✅ |
| No credentials in repo | ✅ |
| Uses variables + tfvars | ✅ |

---

