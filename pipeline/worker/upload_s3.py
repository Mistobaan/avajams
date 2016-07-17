
import boto
import boto.s3
import sys
from boto.s3.key import Key
import os

def file_exists_s3(filename):
    bucket_name = "avajams"
    conn = boto.connect_s3()

    bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

    try:
        conn.head_object(Bucket=bucket_name, Key=filename)
        return True 
    except Exception,e:
        # Not found
        return False

def upload_s3(filename):
    bucket_name = "avajams"
    conn = boto.connect_s3()

    bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

    if file_exists_s3(filename):
        return

    k = Key(bucket)
    k.key = os.path.split(filename)[-1]
    k.set_contents_from_filename(filename)
