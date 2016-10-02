import json, urllib2, hashlib, datetime, time
import boto3, gzip

# insert your credentials for corezoid process here
conv_id = # integer
api_login = # integer
secret_key = "" # string

api_url = "https://www.corezoid.com/api/1/json"
s3 = boto3.client('s3')

def date_to_unixtime(date_obj):
    return int(time.mktime(date_obj.timetuple()))

def get_signature(event, time, req):
    body = ''.join(map(str,[time, secret_key, req, secret_key]))
    return hashlib.sha1(body).hexdigest()

def get_content_from_event(bucket_name, key_name):
    s3.download_file(bucket_name, key_name, '/tmp/ct.gz')
    with gzip.open('/tmp/ct.gz', 'rb') as f:
        content = f.read()
    return content

def push_to_corezoid(request):
	headers = { 'Content-type': 'application/json; charset=utf8' }
	request = json.dumps(request, separators=(',',':'))

	unixtime = date_to_unixtime(datetime.datetime.now())
	signature = get_signature(request, unixtime, request)
	url = '/'.join(map(str, [ api_url, api_login, unixtime, signature ]))
	req = urllib2.Request(url, request, headers)
	response = urllib2.urlopen(req)
	return response.read()

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    data = json.loads(get_content_from_event(bucket, key))
    request = { 'ops': [] }

    for i in data['Records']:
        request['ops'].append({ 'type': 'create', 'obj': 'task', 'conv_id': conv_id, 'data': i })

    response = push_to_corezoid(request)
    return response
