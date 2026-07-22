# Auto Scaling

## Overview

Amazon EC2 Auto Scaling automatically adjusts the number of EC2 instances based on application demand.

This improves availability while optimizing infrastructure costs.

---

## Benefits

- Automatic Scaling
- High Availability
- Self Healing
- Cost Optimization

---

## Scaling Policy

Example configuration:

Minimum Capacity

2 Instances

Desired Capacity

2 Instances

Maximum Capacity

4 Instances

Scale Out

CPU > 70%

Scale In

CPU < 30%

---

## Architecture

```
                Auto Scaling Group

              Minimum : 2

              Desired : 2

              Maximum : 4

        +-------------------------+

        EC2 Instance (AZ-1)

        EC2 Instance (AZ-2)

        EC2 Instance (Optional)

        EC2 Instance (Optional)

        +-------------------------+
```

---

## Health Checks

The Auto Scaling Group continuously monitors instance health.

If an instance becomes unhealthy:

1. Terminate unhealthy instance
2. Launch replacement instance
3. Register with Load Balancer
4. Restore desired capacity

---

## Best Practices

- Distribute instances across multiple Availability Zones.
- Use Launch Templates instead of Launch Configurations.
- Enable detailed monitoring.
- Use lifecycle hooks when appropriate.