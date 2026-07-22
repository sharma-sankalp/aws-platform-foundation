# Application Load Balancer

## Overview

The Application Load Balancer (ALB) distributes incoming HTTP and HTTPS traffic across multiple EC2 instances.

It acts as the single entry point for client requests and improves both scalability and availability.

---

## Responsibilities

- Traffic Distribution
- Health Checks
- SSL Termination
- Path-based Routing
- Host-based Routing

---

## Architecture

```
                  Internet

                      │

         Application Load Balancer

              │               │

         EC2 Instance     EC2 Instance

             AZ-1             AZ-2
```

---

## Health Checks

The ALB periodically checks the health of backend instances.

If an instance fails:

- Stop routing traffic
- Route requests to healthy instances
- Resume traffic once recovered

---

## Benefits

- High Availability
- Fault Tolerance
- Automatic Traffic Distribution
- Improved Performance
- Better User Experience

---

## Best Practices

- Deploy ALB across multiple Availability Zones.
- Enable HTTPS using ACM certificates.
- Configure access logs.
- Integrate with AWS WAF when exposing public applications.