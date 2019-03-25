import AccountType


class AccountHolder:

    def __init__(self, first_name, surname, dob, email, address):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.accountId = email
        self.type = "CURRENT"


