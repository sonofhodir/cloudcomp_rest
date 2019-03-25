from __future__ import print_function  # Python 2/3 compatibility
import boto3

from database.Connection import Connection


class CreateSchema(Connection):
    def __init__(self, database_name, region_name, endpoint_url):
        super().__init__(database_name, region_name, endpoint_url)

    def delete_table(self):
        table_name = 'Account'
        table_names = [table.name for table in self.dynamodb.tables.all()]
        if table_name in table_names:
            self.dynamodb.Table('Account').delete()

    def create_table(self):
        try:
            self.delete_table()
            table = self.dynamodb.create_table(
                TableName='Account',
                KeySchema=[
                    {
                        'AttributeName': 'accountId',
                        'KeyType': 'HASH'  # Partition key -- important to have one account in one partition (not spread)
                    },
                    {
                        'AttributeName': 'date',
                        'KeyType': 'RANGE'  # Sort key -- as transactions always accessed by date
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'accountId',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'date',
                        'AttributeType': 'S'
                    # Date	S (string type). The Date values are stored as ISO-8601 formatted strings
                    },

                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1,
                }
            )
            #print("Table status:", table.table_status)
        except:
            print("Table created")



