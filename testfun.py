import json
import boto3
import csv

#S3=boto3.resource('s3')
s3=boto3.client('s3')

def lambda_handler(event, context):
    buckety='demo-bucket-sih'
    #key='img.png'
    key='file.csv'
    #bucket=S3.Bucket(buckety)
    '''
    for bucket in s3.buckets.all():
        print(bucket)
        for key in bucket.objects.all():
            print(key.key)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()        
    
    '''
    
    '''
    print(bucket)
    for obj in bucket.objects.all():
        key = obj.key
        print(key)
        #body = obj.get()['Body'].read()
    '''
    #print(bucket)
    
    
    '''
    s3_object = s3.get_object(Bucket=buckety, Key=key)
    body = s3_object['Body']
    print(body.read())
    key='requirements.txt'
    s3_object = s3.get_object(Bucket=buckety, Key=key)
    body = s3_object['Body'].read()
    print(body)
    
    '''
    key='img.png'
    s3_object = s3.get_object(Bucket=buckety, Key=key)
    body = s3_object['Body'].read()
    print(body)
    
    
    
    
        
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
