# EBS Snapshot Cleanup

## Overview

This project automates the cleanup of outdated Amazon EBS snapshots using AWS Lambda.

The function runs on a scheduled basis through Amazon EventBridge, identifies snapshots older than a configurable retention period, deletes eligible snapshots, and publishes a notification using Amazon SNS.

This helps reduce storage costs while ensuring that recent snapshots remain available for recovery.

---

## Architecture

```

EventBridge Schedule

↓

AWS Lambda

↓

Describe EBS Snapshots

↓

Delete Expired Snapshots

↓

Publish SNS Notification

↓

CloudWatch Logs

```

---

## Objectives

- Reduce unnecessary EBS snapshot storage costs
- Automate infrastructure maintenance
- Minimize manual operational effort
- Maintain operational visibility through CloudWatch Logs
- Notify administrators after every cleanup run

---

## Features

- Configurable snapshot retention period
- Tag-based snapshot selection
- Automatic deletion of eligible snapshots
- Structured logging using Python logging module
- CloudWatch integration
- Amazon SNS notifications
- Environment variable configuration
- Exception handling

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| RETENTION_DAYS | Number of days to retain snapshots | 7 |
| SNS_TOPIC_ARN | SNS topic for notifications | Optional |
| SNAPSHOT_TAG_KEY | Tag key used to identify managed snapshots | AutoCleanup |
| SNAPSHOT_TAG_VALUE | Required tag value | true |

---

## Workflow

1. EventBridge triggers the Lambda function.
2. Lambda retrieves all snapshots owned by the AWS account.
3. Snapshots are filtered by the configured tag.
4. Snapshot age is compared with the retention period.
5. Eligible snapshots are deleted.
6. A cleanup summary is published to Amazon SNS.
7. Execution logs are written to CloudWatch.

---

## Future Improvements

- Multi-region cleanup
- Cross-account support
- Dry-run mode
- Snapshot reporting dashboard
- Unit tests
