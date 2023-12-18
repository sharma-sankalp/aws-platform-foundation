python
Copy code
import boto3
import datetime

def lambda_handler(event, context):
    # Connect to AWS services
    ec2 = boto3.client('ec2')
    
    # Get a list of all EBS snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    # Find unused snapshots
    unused_snapshots = find_unused_snapshots(snapshots)
    
    # Delete or notify about unused snapshots
    for snapshot in unused_snapshots:
        # Delete or send notification logic goes here
        # Example: ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
        print(f"Unused snapshot found: {snapshot['SnapshotId']}")

def find_unused_snapshots(snapshots):
    unused_snapshots = []
    current_time = datetime.datetime.now(datetime.timezone.utc)
    
    for snapshot in snapshots:
        # Define your criteria for identifying unused snapshots
        # Example: If the snapshot is older than 7 days, consider it unused
        snapshot_time = snapshot['StartTime'].replace(tzinfo=datetime.timezone.utc)
        if (current_time - snapshot_time).days > 7:
            unused_snapshots.append(snapshot)
    
    return unused_snapshots
