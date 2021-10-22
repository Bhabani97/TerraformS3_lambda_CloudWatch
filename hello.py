import json

import boto3
import urllib



def welcome(event, context):
    s3 = boto3.client("s3")
    print(event)
    if event:
       # file_obj = event["Records"][0]
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        filename = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"],encoding="utf-8")
        print(f"Filename : {filename},bucket_name : {bucket_name}")
        file_object = s3.get_object(Bucket="my-test-bucket-terraform1997", Key=filename)
       
        file_content = file_object["Body"].read().decode("utf-8")
        print((file_content))

    return {
        'statusCode' : 200,
        'body' : json.dumps("Hello from Lambda!")
    }

