import json

import boto3

S3_BUCKET = "corporate-drones-music-league"
OBJECT_KEY = "round_results.json"

def handler(event, context):
    return _get_json_body()


def _get_json_body():
    print("Getting json from s3...")
    s3_client = boto3.client("s3")
    return json.load(s3_client.get_object(Bucket=S3_BUCKET, Key=OBJECT_KEY)["Body"])

if __name__ == '__main__':
    _get_json_body()