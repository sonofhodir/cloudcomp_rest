import datetime

from RestServiceImpl import RestServiceImpl
from Transaction import Transaction


class Account:

    def __init__(self, account, balance=0.00):
        self.account = account
        self._balance = balance  #_ indicates "private" properties
        self.rest_service_impl = RestServiceImpl()

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        transaction = Transaction(datetime.datetime.today(), amount, 0, self.balance)
        self.rest_service_impl.record_transaction(self.account, transaction)


    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        transaction = Transaction(datetime.datetime.today(), 0, amount, self._balance)
        self.rest_service_impl.record_transaction(self.account, transaction)

    def print_statement(self):
        self.rest_service_impl.print_statement(self.account)

    def __str__(self):
        return 'Bank account of {} {}, current balance: {}'.format(self.account.first_name, self.account.surname , self.balance)