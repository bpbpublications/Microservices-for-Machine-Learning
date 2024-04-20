
import boto3
s3 = boto3.client('s3')
s3.upload_file('song.mp3', 'mybucket', 'song.mp3')
