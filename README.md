<h2 align="center"> Cloud Computing REST API</h2>
 <p align="center">  <a href='#overview'>Overview</a> |  <a href='#requirements'>Requirements</a>  |   <a href='#example'>Example</a> |  <a href='#links'>Useful Links</a> 

## Python Sample Bank  Account App
### Overview <a name="overview"> </a>
Create a bank app which satisfies the following acceptance criteria:
```
Given a client makes a deposit of 1000 on 10-01-2012
And a deposit of 2000 on 13-01-2012
And a withdrawal of 500 on 14-01-2012
When she prints her bank statement
Then she would see
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```

### Requirements <a name="requirements"> </a>
Make deposits and withdrawals from Bank Account:
- Add unit tests to validate your code
- Push the data to a database (like dynamoDB on AWS)
- Think of Infrastructure as code for your resources
- Run this as a Serverless app with an api to access this  (Serverless allows scaling using AWS Lambda settings)

### Example of running the App <a name="example"> </a>
=> MainDriverTest.py :
```
import datetime
from Account import Account
from AccountHolder import AccountHolder

accountHolder = AccountHolder("Name", "Surname", datetime.datetime(2000, 2, 2), "email@gmail.com", "1 Vitoria Street, London, SW1 6GH")
account = Account(accountHolder, 0)
account.deposit(1000)
account.deposit(3000)
account.withdraw(500)
account.print_statement()
```

=> CURL access: (XXX is the endpoint to connect to)
curl -X POST https://XXX.execute-api.us-east-1.amazonaws.com/dev/endpoints --data "{ \"text\": { \"accountId\": \"email@gmail.com\", \"first_name\": \"James\", \"surname\": \"Smith\", \"dob\": \"01/01/2000\", \"address\": \"1 VitoriaStreet, London, SW1 9SU\", \"type\": \"CURRENT\", \"date\": \"12/02/2019\", \"credit\": \"0\", \"debit\": \"500\", \"balance\": \"0\" } }"

curl https://XXX.execute-api.us-east-1.amazonaws.com/dev/endpoints
curl https://XXX.execute-api.us-east-1.amazonaws.com/dev/endpoints/maulenalimbayev@gmail.com



#Note possible to scale this solution with AWS Lambda using serverless set up:
https://serverless.com/examples/aws-python-simple-http-endpoint/


