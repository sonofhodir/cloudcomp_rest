import datetime

from Account import Account
from AccountHolder import AccountHolder
from Transaction import Transaction
from database.CreateSchema import CreateSchema
from database.DatabaseReader import DatabaseReader
from database.DatabaseSink import DatabaseSink


def createTable(): #deletes if exists
        schema = CreateSchema('dynamodb', 'eu-west-2', "http://localhost:8000")
        schema.create_table()

def queryTable():
        temp = DatabaseReader("dynamodb", "eu-west-2", "http://localhost:8000")
        accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com",
                                      "1 Vitoria Street, London, SW1 6GH")
        account = Account(accountHolder, 0)
        temp.get_statement(account)

def insertIntoTable():
    temp = DatabaseSink("dynamodb", "eu-west-2", "http://localhost:8000")
    accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com",
                                  "1 Vitoria Street, London, SW1 6GH")
    transaction = Transaction(datetime.datetime.today(), 0, 500, 500)
    temp.record_transaction(accountHolder, transaction)




if __name__ == '__main__':
    createTable()
    insertIntoTable()
    queryTable()