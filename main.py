import json

import boto3

S3_BUCKET = "corporate-drones-music-league"
DICTATOR_LEAGUE_OBJECT_KEY = "dictator_league.json"
CORPORATE_DRONES_OBJECT_KEY = "corporate_drones.json"

def handler(event, context):
    path = event.get("path")
    resp = {}
    print(f"{path} endpoint invoked")
    if path == "/all" or path ==  "/":
        dictator_league_body = _get_json_body(DICTATOR_LEAGUE_OBJECT_KEY)
        corporate_drones_body = _get_json_body(CORPORATE_DRONES_OBJECT_KEY)
        # Combine both league rounds
        dictator_league_body.get("rounds").extend(corporate_drones_body.get("rounds"))
        resp = dictator_league_body
    elif path == "/corporate-drones":
        resp = _get_json_body(CORPORATE_DRONES_OBJECT_KEY)
    elif path == "/dictator-league":
        resp = _get_json_body(DICTATOR_LEAGUE_OBJECT_KEY)
    else:
        return {"error": f"path {path} not a valid path"}

    return resp


def _get_json_body(object_key):
    print(f"Getting {object_key} from s3...")
    s3_client = boto3.client("s3")
    return json.load(s3_client.get_object(Bucket=S3_BUCKET, Key=object_key)["Body"])

if __name__ == '__main__':
    event = {"path": "/dictator-league"}
    with open("test.json", "w") as outfile:
        outfile.write(json.dumps(handler(event, None)))