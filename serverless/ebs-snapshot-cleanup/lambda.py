import json
import logging
import os
from datetime import datetime, timezone
from typing import Any

import boto3
from botocore.exceptions import ClientError

# =============================================================================
# Logging Configuration
# =============================================================================

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# =============================================================================
# AWS Clients
# =============================================================================

ec2 = boto3.client("ec2")
sns = boto3.client("sns")

# =============================================================================
# Environment Variables
# =============================================================================

RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "7"))
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

SNAPSHOT_OWNER = os.getenv("SNAPSHOT_OWNER", "self")

SNAPSHOT_TAG_KEY = os.getenv("SNAPSHOT_TAG_KEY", "AutoCleanup")
SNAPSHOT_TAG_VALUE = os.getenv("SNAPSHOT_TAG_VALUE", "true")

DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    AWS Lambda entry point.

    Deletes EBS snapshots that:
    - belong to the configured owner
    - are older than the configured retention period
    - contain the required management tag
    """

    logger.info("Starting EBS Snapshot Cleanup")

    try:
        snapshots = ec2.describe_snapshots(
            OwnerIds=[SNAPSHOT_OWNER]
        )["Snapshots"]

        logger.info("Discovered %d snapshot(s).", len(snapshots))

        expired_snapshots = find_expired_snapshots(snapshots)

        logger.info(
            "%d snapshot(s) matched cleanup criteria.",
            len(expired_snapshots),
        )

        deleted_snapshots: list[str] = []
        failed_snapshots: list[str] = []

        for snapshot in expired_snapshots:

            snapshot_id = snapshot["SnapshotId"]

            try:
                if DRY_RUN:
                    logger.info(
                        "DRY RUN: Snapshot %s would be deleted.",
                        snapshot_id,
                    )
                    continue

                logger.info(
                    "Deleting snapshot %s.",
                    snapshot_id,
                )

                ec2.delete_snapshot(
                    SnapshotId=snapshot_id
                )

                deleted_snapshots.append(snapshot_id)

            except ClientError:
                logger.exception(
                    "Failed to delete snapshot %s.",
                    snapshot_id,
                )

                failed_snapshots.append(snapshot_id)

        publish_summary(
            deleted_snapshots,
            failed_snapshots,
        )

        logger.info("Snapshot cleanup completed.")

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "retention_days": RETENTION_DAYS,
                    "dry_run": DRY_RUN,
                    "snapshots_scanned": len(snapshots),
                    "eligible_snapshots": len(expired_snapshots),
                    "deleted_snapshots": deleted_snapshots,
                    "failed_snapshots": failed_snapshots,
                },
                indent=2,
            ),
        }

    except ClientError:
        logger.exception("AWS API request failed.")
        raise

    except Exception:
        logger.exception("Unexpected error occurred.")
        raise


def find_expired_snapshots(
    snapshots: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Return snapshots that satisfy all cleanup conditions.
    """

    eligible_snapshots = []

    current_time = datetime.now(timezone.utc)

    for snapshot in snapshots:

        snapshot_age = (
            current_time - snapshot["StartTime"]
        ).days

        tags = {
            tag["Key"]: tag["Value"]
            for tag in snapshot.get("Tags", [])
        }

        if (
            snapshot_age > RETENTION_DAYS
            and tags.get(SNAPSHOT_TAG_KEY) == SNAPSHOT_TAG_VALUE
        ):

            eligible_snapshots.append(snapshot)

            logger.info(
                "Eligible: %s (%d days old)",
                snapshot["SnapshotId"],
                snapshot_age,
            )

        else:

            logger.debug(
                "Skipping snapshot %s.",
                snapshot["SnapshotId"],
            )

    return eligible_snapshots


def publish_summary(
    deleted_snapshots: list[str],
    failed_snapshots: list[str],
) -> None:
    """
    Publish cleanup results to Amazon SNS.
    """

    if not SNS_TOPIC_ARN:
        logger.info(
            "SNS_TOPIC_ARN not configured. Notification skipped."
        )
        return

    message = f"""
EBS Snapshot Cleanup Completed

Retention Period : {RETENTION_DAYS} day(s)

Dry Run          : {DRY_RUN}

Deleted Snapshots : {len(deleted_snapshots)}
Failed Snapshots  : {len(failed_snapshots)}

Deleted
---------
{chr(10).join(deleted_snapshots) if deleted_snapshots else "None"}

Failed
--------
{chr(10).join(failed_snapshots) if failed_snapshots else "None"}
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="EBS Snapshot Cleanup Report",
        Message=message,
    )

    logger.info("SNS notification published successfully.")