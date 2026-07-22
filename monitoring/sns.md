# Monitoring and Notifications

## Overview

Amazon CloudWatch continuously collects operational metrics and logs from AWS resources.

Amazon EventBridge evaluates configured rules and automatically invokes AWS Lambda functions based on scheduled events or infrastructure changes.

Amazon SNS delivers notifications to subscribed users, enabling rapid response to operational events.

Together these services create an automated monitoring and alerting solution.

---

## Architecture

```
              CloudWatch

                   │

             EventBridge Rule

                   │

              AWS Lambda

                   │

             Amazon SNS

                   │

         Email / SMS Notification
```

---

## Objectives

- Detect operational events
- Trigger automated workflows
- Notify administrators
- Reduce manual operational effort

---

## Monitoring Workflow

1. CloudWatch collects metrics.
2. EventBridge evaluates scheduled rules.
3. Lambda performs automated actions.
4. SNS publishes notifications.
5. Engineers receive alerts.

---

## Example Use Cases

- Unused EBS Snapshot Cleanup
- Daily Infrastructure Validation
- Backup Verification
- Cost Optimization Tasks
- Compliance Checks

---

## Benefits

- Automated Operations
- Reduced Manual Intervention
- Faster Incident Response
- Improved Visibility
- Event-Driven Architecture

---

## Best Practices

- Use descriptive EventBridge rule names.
- Enable CloudWatch Logs for all Lambda functions.
- Configure SNS subscriptions with multiple recipients.
- Monitor Lambda failures using CloudWatch Alarms.
- Enable dead-letter queues for critical workloads.

---

## Future Improvements

- PagerDuty Integration
- Slack Notifications
- AWS Chatbot
- CloudWatch Dashboards
- Amazon EventBridge Scheduler