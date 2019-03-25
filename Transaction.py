class Transaction:
    def __init__(self, date, credit, debit, balance):
        self.date = date
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def __str__(self):
        return '{} || {} || {} || {} '.format(self.date.strftime('%d/%m/%Y'), self.credit, self.debit, self.balance)