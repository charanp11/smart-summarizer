import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME

AWS_REGION = "us-west-1"

s3 = boto3.client('s3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_file_to_s3(file_path, filename):
    s3.upload_file(file_path, S3_BUCKET_NAME, filename)
    return generate_presigned_url(filename)  

def generate_presigned_url(filename, expires_in=3600):
    return s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': S3_BUCKET_NAME, 'Key': filename},
        ExpiresIn=expires_in
    )
