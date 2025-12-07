
variable "project_name" { default = "simple-time-service" }
variable "aws_region"   { default = "eu-west-1" }
variable "vpc_cidr"     { default = "10.0.0.0/16" }

variable "container_image" {
  description = "Docker image"
  default     = "your-dockerhub-user/simple-time-service:latest"
}

variable "container_port" { default = 8080 }
variable "task_cpu"       { default = 256 }
variable "task_memory"    { default = 512 }
variable "desired_count"  { default = 1 }
