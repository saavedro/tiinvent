import argparse
import boto3

def s3_list_bucket(bucket_name):
    # TODO implement listing bucket
    #https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    for s3_object in bucket.objects.all():
        print(s3_object)

def s3_download_file(bucket_name, object_name, filename):
    # TODO implement downloading file
    pass

def s3_upload_file(filename, bucket_name, object_name):
    # TODO implement downloading file
    pass    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple S3 CLI')
    subparser = parser.add_subparsers(dest='cmd')
    ls_cmd = subparser.add_parser('ls')
    ls_cmd.add_argument('bucket', help="bucket to list")

    cp_cmd = subparser.add_parser('cp')
    cp_cmd.add_argument('source', help="source file")
    cp_cmd.add_argument('target', help="target file")

    args = parser.parse_args()
    print(args)
    if args.cmd == "ls":
        s3_list_bucket(args.bucket)
    
