import boto3
import pandas as pd
from io import StringIO
from botocore.exceptions import ClientError


# ============================================================
# CONFIGURATION
# ============================================================

REGION = "ap-south-1"

INPUT_BUCKET = "airtport-input-123456789"
OUTPUT_BUCKET = "airtupport-output-123456789"

DATASET_FILE = "ai_dataset.csv"
CONFIG_FILE = "model_config.json"

INPUT_DATASET_KEY = "dataset/ai_dataset.csv"
INPUT_CONFIG_KEY = "config/model_config.json"

OUTPUT_KEY = "predictions/predictions.csv"


# ============================================================
# CREATE S3 CLIENT
# ============================================================

s3 = boto3.client(
    "s3",
    region_name=REGION
)

print("Connected to S3")


# ============================================================
# CREATE BUCKET
# ============================================================

def create_bucket(bucket_name):

    try:

        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }
        )

        print(f"Bucket created: {bucket_name}")

    except ClientError as e:

        error_code = e.response["Error"]["Code"]

        if error_code == "BucketAlreadyOwnedByYou":

            print(f"Bucket already exists: {bucket_name}")

        else:

            raise


# ============================================================
# CREATE INPUT AND OUTPUT BUCKETS
# ============================================================

create_bucket(INPUT_BUCKET)

create_bucket(OUTPUT_BUCKET)


# ============================================================
# UPLOAD DATASET
# ============================================================

print("\nUploading AI dataset...")

s3.upload_file(
    DATASET_FILE,
    INPUT_BUCKET,
    INPUT_DATASET_KEY
)

print(
    f"s3://{INPUT_BUCKET}/{INPUT_DATASET_KEY}"
)


# ============================================================
# UPLOAD CONFIGURATION
# ============================================================

print("\nUploading model configuration...")

s3.upload_file(
    CONFIG_FILE,
    INPUT_BUCKET,
    INPUT_CONFIG_KEY
)

print(
    f"s3://{INPUT_BUCKET}/{INPUT_CONFIG_KEY}"
)


# ============================================================
# READ DATASET FROM S3
# ============================================================

print("\nReading dataset from S3...")

response = s3.get_object(
    Bucket=INPUT_BUCKET,
    Key=INPUT_DATASET_KEY
)

df = pd.read_csv(
    response["Body"]
)

print("\nDataset loaded from S3:")

print(df)


# ============================================================
# SIMPLE AI-STYLE CLASSIFICATION
# ============================================================

print("\nRunning customer support classification...")

def classify_ticket(text):

    text = text.lower()

    if any(word in text for word in [
        "payment",
        "charged",
        "money",
        "transaction"
    ]):
        return "payment"

    elif any(word in text for word in [
        "password",
        "login",
        "locked",
        "account"
    ]):
        return "authentication"

    elif any(word in text for word in [
        "slow",
        "performance",
        "load"
    ]):
        return "performance"

    else:
        return "account"


df["predicted_category"] = df["text"].apply(
    classify_ticket
)

print("\nPredictions:")

print(
    df[
        [
            "ticket_id",
            "text",
            "priority",
            "predicted_category"
        ]
    ]
)


# ============================================================
# WRITE OUTPUT TO NEW S3 BUCKET
# ============================================================

print("\nWriting predictions to output S3 bucket...")

csv_buffer = StringIO()

df.to_csv(
    csv_buffer,
    index=False
)

s3.put_object(
    Bucket=OUTPUT_BUCKET,
    Key=OUTPUT_KEY,
    Body=csv_buffer.getvalue(),
    ContentType="text/csv"
)

print(
    f"Output written to:"
    f"\ns3://{OUTPUT_BUCKET}/{OUTPUT_KEY}"
)


# ============================================================
# LIST OUTPUT BUCKET
# ============================================================

print("\nOutput bucket contents:")

response = s3.list_objects_v2(
    Bucket=OUTPUT_BUCKET
)

for obj in response.get("Contents", []):

    print(
        obj["Key"],
        obj["Size"],
        "bytes"
    )


print("\nAI S3 pipeline completed!")



#================================ Output===============================

# (s3env) ubuntu@ip-172-31-0-22:~/ai$ python3 s3_ai_pipeline.py
# Connected to S3
# Bucket created: airt-support-input-123456789
# Bucket created: airt-support-output-123456789

# Uploading AI dataset...
# s3://airt-support-input-123456789/dataset/ai_dataset.csv

# Uploading model configuration...
# s3://airt-support-input-123456789/config/model_config.json

# Reading dataset from S3...

# Dataset loaded from S3:
#   ticket_id                                               text priority
# 0      T001  My payment was deducted but my order was not p...     high
# 1      T002              I forgot my password and cannot login   medium
# 2      T003                 The application is very slow today   medium
# 3      T004             I was charged twice for the same order     high
# 4      T005                 How can I change my email address?      low
# 5      T006  My account has been locked after multiple logi...     high
# 6      T007            The dashboard takes a long time to load   medium
# 7      T008            I want to update my billing information      low
# 8      T009  Money was deducted from my account but the tra...     high
# 9      T010                        How do I reset my password?      low

# Running customer support classification...

# Predictions:
#   ticket_id                                               text priority predicted_category
# 0      T001  My payment was deducted but my order was not p...     high            payment
# 1      T002              I forgot my password and cannot login   medium     authentication
# 2      T003                 The application is very slow today   medium        performance
# 3      T004             I was charged twice for the same order     high            payment
# 4      T005                 How can I change my email address?      low            account
# 5      T006  My account has been locked after multiple logi...     high     authentication
# 6      T007            The dashboard takes a long time to load   medium        performance
# 7      T008            I want to update my billing information      low            account
# 8      T009  Money was deducted from my account but the tra...     high            payment
# 9      T010                        How do I reset my password?      low     authentication

# Writing predictions to output S3 bucket...
# Output written to:
# s3://airt-support-output-123456789/predictions/predictions.csv

# Output bucket contents:
# predictions/predictions.csv 681 bytes

# AI S3 pipeline completed!