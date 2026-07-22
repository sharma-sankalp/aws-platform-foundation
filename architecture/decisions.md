# Architecture Decisions

This document captures the key architectural decisions made while designing this AWS reference platform.

---

## Decision 1 - Private Database

**Decision**

Deploy Amazon RDS in private subnets.

**Reason**

Databases should not be directly accessible from the internet. Access is restricted to trusted application servers using Security Groups.

---

## Decision 2 - Auto Scaling

**Decision**

Use an Auto Scaling Group to manage EC2 instances.

**Reason**

This improves availability, enables self-healing, and automatically adjusts capacity based on demand.

---

## Decision 3 - Application Load Balancer

**Decision**

Place an Application Load Balancer in front of the application.

**Reason**

The ALB distributes traffic across multiple EC2 instances and performs health checks to route traffic only to healthy targets.

---

## Decision 4 - Event-Driven Automation

**Decision**

Schedule AWS Lambda using Amazon EventBridge.

**Reason**

Scheduled serverless execution removes the need for dedicated management servers while reducing operational overhead.

---

## Decision 5 - Tag-Based Snapshot Cleanup

**Decision**

Delete only snapshots explicitly tagged for automated cleanup.

**Reason**

This prevents accidental deletion of manually created or long-term backup snapshots.

---

## Decision 6 - Environment Variables

**Decision**

Store runtime configuration in Lambda environment variables.

**Reason**

This improves portability across environments and avoids hardcoded values.

---

## Decision 7 - Least Privilege IAM

**Decision**

Grant the Lambda execution role only the permissions required for snapshot cleanup, SNS publishing, and CloudWatch logging.

**Reason**

Following the principle of least privilege reduces the impact of compromised credentials.

---

## Future Enhancements

- Infrastructure as Code using Terraform
- GitHub Actions CI/CD
- Multi-Region deployment
- Amazon EKS integration
- AWS WAF
- AWS Config
- GuardDuty
- CloudTrail