# Terraform Infrastructure (Task 2)

This folder contains Terraform code to deploy a **containerized web service** onto AWS using **ECS Fargate**, running inside a secure VPC and exposed via an Application Load Balancer (ALB).


---

## 📌 Infrastructure Created

Terraform provisions the following AWS resources:

### **Networking**
- VPC 
- 2 public subnets  
- 2 private subnets  
- Internet Gateway  
- NAT Gateway  
- Public + Private Route Tables  

### **Compute (ECS Fargate)**
- ECS Cluster
- ECS Task Definition (Fargate)
- ECS Service running in **private subnets only**
- CloudWatch Log Group

### **Load Balancer**
- Application Load Balancer in **public subnets**
- Target group
- Listener (port 80)

### **IAM**
- ECS task execution role  
- ECS task role  

---

## 📁 Folder Structure

```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
└── README.md
```

---

## 🛠 Prerequisites

### **1. Terraform v1.5+**
Install: https://developer.hashicorp.com/terraform/downloads  

### **2. AWS Credentials (DO NOT commit them)**  
Authenticate using any one of:

#### Option A — Environment variables:
```
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="xxx"
export AWS_DEFAULT_REGION="eu-west-1"
```

#### Option B — AWS CLI profile:
```
aws configure --profile myprofile
export AWS_PROFILE=myprofile
```

#### Option C — AWS SSO:
If SSO is configured, Terraform will use it automatically.

---

## 🔧 Configure Before Running

Edit `terraform.tfvars` and set:

```
container_image = "your-dockerhub-username/simple-time-service:latest"
```

You may replace the image name with any container image you want to deploy.

---

## ▶️ Deployment Steps

### **1. Plan**
```
terraform plan
```

### **2. Apply**
```
terraform apply
```

Approve with **yes**.

Terraform will:
- Create all networking
- Deploy the ECS cluster
- Create IAM roles
- Launch your container in private subnets
- Attach the ALB

---

## 🌍 Testing

Get the ALB DNS name:

```
terraform output -raw alb_dns_name
```

Test it:

```
curl http://<alb_dns_name>/
```

You should receive the container’s HTTP response.

---

## 🧹 Destroy Infrastructure (Important)

```
terraform destroy
```

Approve with **yes**.

This removes all created AWS resources.

---

## ✔️ Requirement Mapping

| Requirement | Status |
|------------|--------|
| VPC with 2 public + 2 private subnets | ✅ Done |
| ECS/EKS or equivalent | ✅ ECS Fargate |
| Container runs only in private subnets | ✅ Done |
| Public ALB directing to service | ✅ Done |
| `terraform plan` + `terraform apply` only | ✅ Yes |
| No credentials committed | ✅ Yes |
| Variables + tfvars used | ✅ Yes |
| Clean, documented Terraform | ✅ Yes |

---

## ⚠️ IAM Permissions Required

Your AWS user **must** have permissions like:

- `ecs:*`
- `iam:CreateRole`
- `iam:PassRole`
- `logs:CreateLogGroup`
- `ec2:*`
- `elasticloadbalancing:*`

If you see **AccessDenied**, your IAM user needs additional privileges.

---

