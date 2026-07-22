# VPC Peering

## Overview

Amazon VPC Peering enables private network connectivity between two Virtual Private Clouds (VPCs). Resources within each VPC can communicate using private IP addresses without traversing the public internet.

This architecture is commonly used when applications, shared services, or databases are deployed in separate VPCs but require secure communication.

---

## Use Cases

Typical use cases include:

- Shared services VPC
- Centralized logging
- Shared monitoring
- Development and Production connectivity
- Cross-account networking
- Database access
- Microservice communication

---

## Architecture

```
          VPC A
     10.0.0.0/16
          │
          │
   VPC Peering Connection
          │
          │
          VPC B
     10.1.0.0/16
```

Traffic remains on the AWS backbone and does not traverse the public internet.

---

## Components

### Amazon VPC

Provides logical isolation for AWS resources.

### Route Tables

Each VPC must contain routes that point traffic destined for the remote CIDR block to the VPC Peering Connection.

### Security Groups

Security Groups must explicitly allow traffic from the remote VPC.

### Network ACLs

Network ACLs should also permit the required traffic.

---

## Implementation Steps

1. Create two VPCs with non-overlapping CIDR ranges.
2. Create a VPC Peering Connection.
3. Accept the peering request.
4. Update Route Tables in both VPCs.
5. Update Security Groups.
6. Validate connectivity.

---

## Advantages

- Private communication
- Low latency
- No VPN required
- No internet exposure
- Simple to configure

---

## Limitations

- No transitive routing
- Overlapping CIDR blocks are not supported
- Route management becomes complex with many VPCs

---

## Best Practices

- Use meaningful CIDR planning.
- Follow least-privilege Security Group rules.
- Enable VPC Flow Logs.
- Use AWS Transit Gateway for large-scale environments instead of excessive VPC peering.

---

## References

- AWS VPC Documentation
- AWS Well-Architected Framework