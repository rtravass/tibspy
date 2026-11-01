import boto3
import pandas as pd

from io import StringIO
from botocore.exceptions import ClientError

from avi.sdk.avi_api import ApiSession



REGION = "ap-south-1"

DATASET_FILE = "ai_dataset.csv"
CONFIG_FILE = "model_config.json"

INPUT_DATASET_KEY = "dataset/ai_dataset.csv"
INPUT_CONFIG_KEY = "config/model_config.json"

OUTPUT_KEY = "predictions/predictions.csv"


s3 = boto3.client(
    "s3",
    region_name = REGION
)

sts = boto3.client(
    "sts",
    region_name = REGION
)

#2. get aws account id

identity = sts.get_caller_identity()

ACCOUNT_ID = identity["ACCOUNT"]
print("AWS Account ID: ", ACCOUNT_ID)
print("AWS Region: ", REGION)


#3. create buckets

INPUT_BUCKET = (
    f"ai-support-input-{ACCOUNT_ID}-{REGION}-an"
)

OUTPUT_BUCKET = (
    f"ai-support-output-{ACCOUNT_ID}-{REGION}-an"
)

print("\nInput bucket: ")
print(INPUT_BUCKET)
print("\nOutput bucket: ")
print(OUTPUT_BUCKET)



#4. create the buckets 

def create_bucket(bucket_name):
    print(f"\nCreating bucket: {bucket_name}")

    try:
        response = s3.create_bucket(
            Bucket = bucket_name
            BucketNamespace = "account-regional"

            CreateBucketConfiguration = {
                "LocationConstraint" : REGION
            }
        )

        print("Bucket created successfully")   #7:47

