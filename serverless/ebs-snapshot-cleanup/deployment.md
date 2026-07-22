# Deployment

## Prerequisites

- AWS Account
- IAM Role for Lambda
- Amazon SNS Topic (Optional)
- EventBridge Rule
- CloudWatch Logs

---

## Environment Variables

| Variable | Value |
|----------|------|
| RETENTION_DAYS | 7 |
| SNS_TOPIC_ARN | arn:aws:sns:region:account:topic |

---

## IAM Permissions

The Lambda execution role requires permissions to:

- Describe EBS Snapshots
- Delete EBS Snapshots
- Publish to Amazon SNS
- Write CloudWatch Logs

---

## Scheduling

The function is intended to run automatically using Amazon EventBridge.

Example Schedule:

```
rate(1 day)
```

---

## Monitoring

Execution logs are available in Amazon CloudWatch Logs.

Failures can be monitored using:

- CloudWatch Metrics
- CloudWatch Alarms
- SNS Notifications