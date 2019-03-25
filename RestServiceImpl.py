import json
import time
import requests

import Constants
from endpoints import decimalencoder


class RestServiceImpl:
    def record_transaction(self, account_holder, transaction):
        timestamp = int(time.time() * 1000)

        item_json = {
            "text": {
                'accountId': account_holder.accountId,
                'date': str(transaction.date.strftime('%d/%m/%Y')),
                'first_name': account_holder.first_name,
                'surname': account_holder.surname,
                'dob': str(account_holder.dob.strftime('%d/%m/%Y')),
                'address': account_holder.address,
                'type': account_holder.type,
                'credit': transaction.credit,
                'debit': transaction.debit,
                'balance': transaction.balance,
                'createdAt': timestamp,
                'updatedAt': timestamp,
            }

        }
        data = json.dumps(item_json,
                          cls=decimalencoder.DecimalEncoder)
        response = requests.post(Constants.ENDPOINT, data=data)
        print('Successfully recorded transaction', response)

    def print_statement(self, account):
        path = Constants.ENDPOINT
        response = requests.get(path)
        json_response = json.loads(response.text)
        print("date || credit || debit || balance")
        for tran in json_response:  #::-1 produces reverse copy [::-1]
            if account.accountId == tran['id']: #had to put workaround temporarily, as querying on non-pk column
                credit = tran['credit'] if tran['credit'] != 0 else ''  # workaround not to print 0, as on persistence need to pass 0
                debit = tran['debit'] if tran['debit'] != 0 else ''
                print('{} || {} || {} || {} '.format(tran['date'],credit , debit, tran['balance']))


