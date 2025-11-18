---
name: terraform-iac
description: Master Terraform for managing cloud infrastructure as code.
---

# Terraform & Infrastructure as Code

## Quick Start

### Main Configuration
```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

## Key Concepts

- **Resources**: Infrastructure components
- **Variables**: Input values
- **Outputs**: Return values
- **State**: Track infrastructure
- **Modules**: Reusable components
- **Providers**: Infrastructure platforms

## Commands

```bash
terraform init          # Initialize
terraform plan          # Preview changes
terraform apply         # Apply changes
terraform destroy       # Destroy infrastructure
terraform state list    # View state
```

## Best Practices

✅ Version control everything
✅ Use modules
✅ Use variables
✅ Implement remote state
✅ Use workspaces
✅ Follow naming conventions
✅ Document infrastructure

