---
name: aws-cloud
description: Master AWS services for building scalable cloud applications.
---

# AWS Cloud Services

## Core Services

### Compute
- **EC2**: Virtual machines, autoscaling
- **Lambda**: Serverless functions
- **ECS**: Docker container orchestration
- **EKS**: Kubernetes on AWS

### Database
- **RDS**: Relational databases
- **DynamoDB**: NoSQL database
- **Aurora**: High-performance relational

### Storage
- **S3**: Object storage
- **EBS**: Block storage
- **EFS**: File storage

### Networking
- **VPC**: Virtual private cloud
- **CloudFront**: CDN
- **ALB**: Load balancing

## Getting Started

```bash
# Configure AWS CLI
aws configure

# Launch EC2 instance
aws ec2 run-instances --image-id ami-xxx

# Upload to S3
aws s3 cp file.txt s3://bucket/
```

## Key Concepts

- **Regions**: Geographic locations
- **Availability Zones**: Independent datacenters
- **IAM**: Identity and access management
- **Security Groups**: Firewall rules
- **Auto Scaling**: Automatic scaling

## Best Practices

✅ Use least privilege IAM
✅ Enable encryption
✅ Use managed services
✅ Monitor costs
✅ Implement disaster recovery
✅ Use infrastructure as code

