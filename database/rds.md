# Amazon RDS

## Overview

Amazon Relational Database Service (Amazon RDS) is a managed database service that simplifies database administration while providing high availability, automated backups, software patching, and monitoring.

In this architecture, Amazon RDS stores the application's persistent data and is accessed only by EC2 instances within the Virtual Private Cloud (VPC).

---

## Objectives

- Store application data securely
- Eliminate database administration overhead
- Improve reliability
- Enable automated backups
- Support disaster recovery

---

## Architecture

```
            EC2 Instances

                 │

          Security Group

                 │

          Amazon RDS MySQL

                 │

          Automated Backups
```

---

## Configuration

Example deployment:

Database Engine

- MySQL

Deployment

- Amazon RDS

Availability

- Single AZ (Lab)
- Multi-AZ (Production)

Storage

- General Purpose SSD (gp3)

Backups

- Automated Daily Backup

Monitoring

- Amazon CloudWatch

---

## Network Design

The database is deployed inside private subnets.

Reasons:

- No direct internet access
- Better security
- Controlled access through Security Groups
- Isolation from public workloads

---

## Security

Best practices include:

- Private subnet deployment
- Least privilege Security Groups
- IAM authentication (where applicable)
- Encryption at rest
- Encryption in transit
- Automated patching

---

## Backup Strategy

The platform supports:

- Automated backups
- Point-in-Time Recovery
- Manual snapshots
- Cross-region snapshot copy (optional)

---

## Disaster Recovery

Production workloads should implement:

- Multi-AZ deployment
- Read Replicas
- Automated failover
- Snapshot retention
- Cross-region backup

---

## Best Practices

- Never expose RDS publicly unless required.
- Enable automated backups.
- Rotate credentials regularly.
- Monitor storage, CPU, memory, and connections.
- Enable Enhanced Monitoring for production workloads.