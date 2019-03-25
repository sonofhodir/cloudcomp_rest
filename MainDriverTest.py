import datetime

from Account import Account
from AccountHolder import AccountHolder

accountHolder = AccountHolder("Maulen", "Alimbayev", datetime.datetime(2000, 2, 2), "email@gmail.com", "1 Vitoria Street, London, SW1 6GH")
account = Account(accountHolder, 0)
account.deposit(1000)
account.deposit(3000)
account.withdraw(500)
account.print_statement()
