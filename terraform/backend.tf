terraform {
  backend "s3" {
    bucket         = "YOUR-TF-STATE-BUCKET-NAME"
    key            = "simple-time-service/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "YOUR-TF-LOCK-TABLE-NAME"
    encrypt        = true
  }
}
