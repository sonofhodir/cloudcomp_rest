import boto3
import json
from database.Connection import Connection


class DatabaseSink(Connection):
    def __init__(self, database_name, region_name, endpoint_url):
        super().__init__(database_name, region_name, endpoint_url)
        self.table = self.dynamodb.Table('Account')

    def record_transaction(self, account_holder, transaction):

        print("Adding event place:", account_holder.first_name, transaction.date)
        self.table.put_item(
            Item={
                'accountId': account_holder.accountId,
                'date': str(transaction.date.isoformat()),
                'first_name': account_holder.first_name,
                'surname': account_holder.surname,
                'dob': str(account_holder.dob.isoformat()),
                'address': account_holder.address,
                'type': account_holder.type,
                'credit': transaction.credit,
                'debit': transaction.debit,
                'balance': transaction.balance,
            }
        )
