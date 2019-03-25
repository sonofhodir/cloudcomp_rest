import boto3
from boto3.dynamodb.conditions import Key, Attr

from database.Connection import Connection


class DatabaseReader(Connection):
    def __init__(self, database_name, region_name, endpoint_url):
        super().__init__(database_name, region_name, endpoint_url)
        self.table = self.dynamodb.Table('Account')

    def get_statement(self, account):
        response = self.table.query(
            KeyConditionExpression=Key('accountId').eq(account.account.accountId)
        )
        print("date || credit || debit || balance")
        for i in response['Items']:
            credit = i['credit'] if i['credit']!= 0 else ''  #workaround not to print 0, as on persistence need to pass 0
            debit = i['debit'] if i['debit']!= 0 else ''
            print(i['date'], "||", credit, "||", debit, "||", i['balance'])
