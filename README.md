# AWS CloudTrail events processing

## Quick Start

### Upload our folder with processes to your Corezoid-account.

Once you have successfully logged in your account click: **Create** -> **From file** and upload 106317_folder.json

![How to upload folder](https://github.com/corezoid/aws-cloudtrail-events-processing/blob/master/upload_folder.png)

### Configure your AWS environment.
1. [Create and configure your trail.](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
2. Replace in **fromCloudTrailToCorezoid.py**: **conv_id**, **api_login** and **secret_key** with your data.
3. [Setup and configure our Lambda function to work with your S3 bucket.](http://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)

### Quick Start with CloudFormation

![How to prepare AWS using CloudFormation](https://github.com/corezoid/aws-cloudtrail-events-processing/blob/master/cloudtrail-corezoid-cf-template.png)
