import boto3
import pandas as pd

from io import StringIO
from botocore.exceptions import ClientError


# ============================================================
# CONFIGURATION
# ============================================================

REGION = "ap-south-1"

DATASET_FILE = "ai_dataset.csv"
CONFIG_FILE = "model_config.json"

INPUT_DATASET_KEY = "dataset/ai_dataset.csv" #S3 bucket/dataset/; buket/config/
INPUT_CONFIG_KEY = "config/model_config.json"

OUTPUT_KEY = "predictions/predictions.csv"


# ============================================================
# 1. CREATE AWS CLIENTS
# ============================================================

s3 = boto3.client(
    "s3",
    region_name=REGION
)

sts = boto3.client(
    "sts",
    region_name=REGION
)


# ============================================================
# 2. GET AWS ACCOUNT ID
# ============================================================

identity = sts.get_caller_identity()

ACCOUNT_ID = identity["Account"]

print("AWS Account ID:", ACCOUNT_ID)
print("AWS Region:", REGION)


# ============================================================
# 3. CREATE ACCOUNT-REGIONAL BUCKET NAMES
# ============================================================

INPUT_BUCKET = (
    f"ai-support-input-{ACCOUNT_ID}-{REGION}-an"
)

OUTPUT_BUCKET = (
    f"ai-support-output-{ACCOUNT_ID}-{REGION}-an"
)


print("\nInput bucket:")
print(INPUT_BUCKET)

print("\nOutput bucket:")
print(OUTPUT_BUCKET)

#create bucket.. uplaoding input files
# ============================================================
# 4. CREATE ACCOUNT-REGIONAL NAMESPACE BUCKET
# ============================================================

def create_bucket(bucket_name):

    print(f"\nCreating bucket: {bucket_name}")

    try:

        response = s3.create_bucket(

            Bucket=bucket_name,

            # IMPORTANT:
            # This creates the bucket in the
            # Account Regional Namespace.
            BucketNamespace="account-regional",

            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }
        )

        print("Bucket created successfully.")

        if "BucketArn" in response:
            print("Bucket ARN:")
            print(response["BucketArn"])

    except ClientError as e:

        error_code = e.response["Error"]["Code"]

        if error_code == "BucketAlreadyOwnedByYou":

            print("Bucket already exists in your account.")

        else:

            print("Bucket creation failed.")
            print(e)
            raise


# ============================================================
# 5. CREATE INPUT AND OUTPUT BUCKETS
# ============================================================

create_bucket(INPUT_BUCKET)

create_bucket(OUTPUT_BUCKET)


# ============================================================
# 6. UPLOAD CSV DATASET
# ============================================================

print("\n--------------------------------")
print("Uploading AI dataset")
print("--------------------------------")

s3.upload_file(
    DATASET_FILE,
    INPUT_BUCKET,
    INPUT_DATASET_KEY
)

print(
    f"Uploaded: s3://{INPUT_BUCKET}/{INPUT_DATASET_KEY}"
)


# ============================================================
# 7. UPLOAD JSON CONFIGURATION
# ============================================================

print("\n--------------------------------")
print("Uploading model configuration")
print("--------------------------------")

s3.upload_file(
    CONFIG_FILE,
    INPUT_BUCKET,
    INPUT_CONFIG_KEY
)

print(
    f"Uploaded: s3://{INPUT_BUCKET}/{INPUT_CONFIG_KEY}"
)


# ============================================================
# 8. LIST INPUT BUCKET OBJECTS
# ============================================================

print("\n--------------------------------")
print("Objects in input bucket")
print("--------------------------------")

response = s3.list_objects_v2(
    Bucket=INPUT_BUCKET
)

for obj in response.get("Contents", []):

    print(
        f"{obj['Key']} "
        f"({obj['Size']} bytes)"
    )


# ============================================================
# 9. READ DATASET FROM S3
# ============================================================

print("\n--------------------------------")
print("Reading dataset from S3")
print("--------------------------------")

response = s3.get_object(
    Bucket=INPUT_BUCKET,
    Key=INPUT_DATASET_KEY
)

df = pd.read_csv(
    response["Body"]
)

print("\nDataset loaded from S3:\n")

print(df)


# ============================================================
# 10. READ MODEL CONFIGURATION FROM S3
# ============================================================

print("\n--------------------------------")
print("Reading model configuration")
print("--------------------------------")

response = s3.get_object(
    Bucket=INPUT_BUCKET,
    Key=INPUT_CONFIG_KEY
)

config_content = response["Body"].read().decode("utf-8")

print(config_content)


# ============================================================
# 11. SIMPLE AI-STYLE CLASSIFICATION
# ============================================================

print("\n--------------------------------")
print("Running AI classification")
print("--------------------------------")


def classify_ticket(text):

    text = text.lower()

    # Payment-related tickets
    if any(word in text for word in [
        "payment",
        "charged",
        "money",
        "transaction"
    ]):

        return "payment"

    # Authentication-related tickets
    elif any(word in text for word in [
        "password",
        "login",
        "locked"
    ]):

        return "authentication"

    # Performance-related tickets
    elif any(word in text for word in [
        "slow",
        "performance",
        "load"
    ]):

        return "performance"

    # Remaining tickets
    else:

        return "account"


df["predicted_category"] = (
    df["text"].apply(classify_ticket)
)


# ============================================================
# 12. DISPLAY PREDICTIONS
# ============================================================

print("\nPredictions:\n")

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
# 13. WRITE OUTPUT TO NEW S3 BUCKET
# ============================================================

print("\n--------------------------------")
print("Writing predictions to S3")
print("--------------------------------")

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
# 14. READ OUTPUT BACK FROM S3
# ============================================================

print("\n--------------------------------")
print("Reading predictions back from S3")
print("--------------------------------")

response = s3.get_object(
    Bucket=OUTPUT_BUCKET,
    Key=OUTPUT_KEY
)

output_df = pd.read_csv(
    response["Body"]
)

print("\nOutput dataset:\n")

print(output_df)


# ============================================================
# 15. LIST OUTPUT BUCKET
# ============================================================

print("\n--------------------------------")
print("Objects in output bucket")
print("--------------------------------")

response = s3.list_objects_v2(
    Bucket=OUTPUT_BUCKET
)

for obj in response.get("Contents", []):

    print(
        f"{obj['Key']} "
        f"({obj['Size']} bytes)"
    )


# ============================================================
# 16. DISPLAY S3 OBJECT URL
# ============================================================

print("\n--------------------------------")
print("S3 Object Information")
print("--------------------------------")

output_url = (
    f"https://{OUTPUT_BUCKET}.s3."
    f"{REGION}.amazonaws.com/"
    f"{OUTPUT_KEY}"
)

print("Output object URL:")
print(output_url)


# ============================================================
# 17. COMPLETED
# ============================================================

print("\n======================================")
print("S3 AI DATASET PIPELINE COMPLETED")
print("======================================")