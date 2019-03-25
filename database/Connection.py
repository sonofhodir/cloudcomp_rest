import boto3


class Connection:
    def __init__(self, database_name, region_name, endpoint_url):
        # self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="http://localhost:8000")
        self.dynamodb = boto3.resource(database_name, region_name=region_name, endpoint_url=endpoint_url)
        
