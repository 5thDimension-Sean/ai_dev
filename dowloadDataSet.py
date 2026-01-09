import boto3
from botocore import UNSIGNED
from botocore.client import Config
import os

#Config for client 
s3 = boto3.client(
    "s3",
    config=Config(signature_version=UNSIGNED)
)

#Specify the feeds from which we want to download data
cameras = ["CAM_FRONT", "CAM_FRONT_RIGHT", "CAM_FRONT_LEFT", "CAM_BACK", "CAM_BACK_LEFT", "CAM_BACK_RIGHT"]

bucket = "motional-nuscenes"

#Loop through each camera feed and download images
for camera in cameras:

    prefix = f"samples/{camera}/"

    local_dir = f"./nuscenes/samples/{camera}"
    os.makedirs(local_dir, exist_ok=True)
paginator = s3.get_paginator("list_objects_v2")

for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
    for obj in page.get("Contents", []):
        key = obj["Key"]
        if key.endswith(".jpg"):
            local_path = os.path.join(local_dir, os.path.basename(key))
            s3.download_file(bucket, key, local_path)