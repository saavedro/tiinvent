#!/usr/bin/env python
import re
import argparse
import logging

import boto3
from botocore.exceptions import ClientError

def s3_list_bucket(bucket_name):
    # TODO implement listing bucket
    #https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    for s3_object in bucket.objects.all():
        print(s3_object)

def s3_download_file(filename, bucket_name, object_name):
    #https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, filename)

def s3_upload_file(filename, bucket_name, object_name):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple S3 CLI')
    subparser = parser.add_subparsers(dest='cmd')
    ls_cmd = subparser.add_parser('ls')
    ls_cmd.add_argument('bucket', help="bucket to list")

    cp_cmd = subparser.add_parser('cp')
    cp_cmd.add_argument('source', help="source file")
    cp_cmd.add_argument('target', help="target file")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()

    if args.cmd == "ls":
        s3_list_bucket(args.bucket)
    elif args.cmd == "cp":
        # Recognize upload or download syntax based on s3:// prefix
        # upload:  s3cli cp file.txt s3://mybucket/file.txt
        # download s3cli cp s3://mybucket/file.txt file.txt
        s3_pattern = r's3://([^/]*)/(.*)'
        m = re.match(s3_pattern, args.source)
        if m: # source is remote => download
            print("Download")
            print(m.group(1,2))
            s3_download_file(filename=args.target, bucket_name=m.group(1), object_name=m.group(2))
        else:
            m = re.match(s3_pattern, args.target)
            if m: # target is remote => upload
                print("Upload")
                print(m.group(1,2))
                s3_upload_file(filename=args.source, bucket_name=m.group(1), object_name=m.group(2))
            else:
                logging.error("No remote path recognized in provided arguments")
