# Amazon EC2

## Overview

Amazon Elastic Compute Cloud (Amazon EC2) provides secure and scalable virtual servers that host application workloads within AWS.

In this architecture, EC2 instances are deployed inside public subnets and serve application traffic received through the Application Load Balancer.

---

## Objectives

- Host the application
- Support Auto Scaling
- Integrate with Load Balancer
- Connect securely to Amazon RDS
- Enable monitoring through CloudWatch

---

## Architecture

```
                Internet
                     │
         Application Load Balancer
                     │
          ┌──────────┴──────────┐
          │                     │
      EC2 Instance         EC2 Instance
        AZ-1                 AZ-2
```

---

## Configuration

Recommended configuration:

- Amazon Linux
- t3.micro / t3.small
- IAM Role attached
- Security Group attached
- CloudWatch Agent
- SSM Agent

---

## Security

- SSH access restricted
- HTTP/HTTPS allowed only through Load Balancer
- IAM Roles used instead of Access Keys
- Security Groups configured using least privilege

---

## Best Practices

- Never deploy production applications on a single EC2 instance.
- Use Auto Scaling for resilience.
- Store application configuration outside the instance where possible.
- Monitor CPU, Memory, and Disk utilization.