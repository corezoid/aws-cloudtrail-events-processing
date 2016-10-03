# AWS CloudTrail events processing

## Quick Start

1. Upload folder with processes to you Corezoid account.

Once you have successfully logged in your account click: **Create** -> **From file** and upload 106317_folder.json

![How to upload folder](https://github.com/corezoid/aws-cloudtrail-events-processing/blob/master/upload_folder.png)

2. [Create and configure your trail.](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
3. Replace in **fromCloudTrailToCorezoid.py**: **conv_id**, **api_login** and **secret_key** with your data.
3. [Setup and configure our Lambda function to work with your S3 bucket.](http://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)
