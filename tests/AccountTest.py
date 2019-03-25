import unittest
import mock
import datetime

from mock import patch

from Account import Account
from AccountHolder import AccountHolder

class TestAccountMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @mock.patch('database.Connection.boto3.resource')
    def test_new_account(self, mock_boto3_resource):
        dynamodb_execute_mock = mock.Mock()
        mock_boto3_resource.return_value = dynamodb_execute_mock
        accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com",
                                      "1 Vitoria Street, London, SW1 6GH")
        account = Account(accountHolder, 0)
        self.assertEqual(account.balance, 0)

    @mock.patch('database.Connection.boto3.resource')
    def test_deposit_account(self, mock_boto3_resource):
        dynamodb_execute_mock = mock.Mock()
        mock_boto3_resource.return_value = dynamodb_execute_mock
        accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com",
                                      "1 Vitoria Street, London, SW1 6GH")
        account = Account(accountHolder, 0)
        account.deposit(1000)
        self.assertEqual(account.balance, 1000)

    @mock.patch('database.Connection.boto3.resource')
    def test_withdraw_account(self, mock_boto3_resource):
        dynamodb_execute_mock = mock.Mock()
        mock_boto3_resource.return_value = dynamodb_execute_mock
        accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com",
                                      "1 Vitoria Street, London, SW1 6GH")
        account = Account(accountHolder, 0)
        account.deposit(1000)
        account.withdraw(500)
        self.assertEqual(account.balance, 500)


if __name__ == '__main__':
    unittest.main()