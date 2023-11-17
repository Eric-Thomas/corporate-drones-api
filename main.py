import json

import boto3

S3_BUCKET = "corporate-drones-music-league"
OBJECT_KEY = "music_league_rounds.json"

def handler(event, context):
    print(event)
    resp = _get_json_body(OBJECT_KEY)
    return resp




def _get_json_body(object_key):
    print(f"Getting {object_key} from s3...")
    s3_client = boto3.client("s3")
    return json.load(s3_client.get_object(Bucket=S3_BUCKET, Key=object_key)["Body"])

if __name__ == '__main__':
    event = {"league": "/dictator-league"}
    with open("test.json", "w") as outfile:
        outfile.write(json.dumps(handler(event, None)))