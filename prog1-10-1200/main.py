import datetime

class Customer:
    def __init__(self, name, surname, id, email):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.datetime_created = datetime.datetime.now()
        self.accounts = []

    def status(self):
        print(f"Client: {self.name} {self.surname} ({self.id}) created: {self.datetime_created}")

    def add_account(self, number, currency, balance):
        self.accounts.append(Account(number, currency, balance))

    def print_accounts(self):
        for account in self.accounts:
            account.status()

    def delete_account(self, account_number):
        found_account = [account for account in self.accounts if account.number == account_number]
        if found_account:
            self.accounts.remove(found_account[0])
            print(f"Account with number {account_number} has been deleted.")
        else:
            print(f"Account with number {account_number} not found.")


# KOMANDAS UZDEVUMS 2
# Izveido Account klases 2 metodes:
# deposit (ielikt naudu kontā)
# withdraw (izneml naudu no konta)
# padomā un piesaisti Transaction klasi Account klasei
# izveido metodi balance Account klasei kas izvada konsolē konta bilanci

class Account:
    def __init__(self, number, currency, balance, account_status = 'Active'):
        self.number = number
        self.currency = currency
        self.balance = balance
        self.datetime_created = datetime.datetime.now()
        self.account_status = account_status
        self.transactions = []

    def status(self):
        print(f"Account: {self.number} ({self.currency}) {self.balance}")

    def deposit(self, amount, notes):
        self.transactions.append(Transaction(amount, notes))
        self.balance += amount

    def withdraw(self, amount, notes):
        self.transactions.append(Transaction(-amount, notes))
        self.balance -= amount

    def print_transactions(self):
        self.status()
        for transaction in self.transactions:
            transaction.status()


class Transaction:
    def __init__(self, amount, notes):
        self.amount = amount
        self.notes = notes
        self.datetime_created = datetime.datetime.now()
    
    def status(self):
        print(f"Transaction:\t{self.amount}\t{self.datetime_created}\t{self.notes}")



# KOMANDAS UZDEVUMS 1
# Izveidot klasi Transaction (jeb darījumi)
# __init__ metode (klases konstruktors)
# status metode (izvadīs konsolē informāciju par konkrēto darījumu)


customer1 = Customer("Anna", "Bērziņa", "123456-789456", "annab@someemail.com")
customer1.add_account("123456789", "EUR", 200)
customer1.add_account("321654987", "USD", 100)
customer1.add_account("8521236575", "JPY", 15000)

customer1.accounts[0].deposit(600, "Alga par 03/2023")
customer1.accounts[0].deposit(20, "par dāvanu")
customer1.accounts[0].withdraw(5, "Pusdienās")
customer1.accounts[0].withdraw(120, "Pirkums veikalā ABC")

customer1.accounts[1].deposit(50, "Freelance compensation")
customer1.accounts[1].withdraw(90, "Amazon.com purchase")

customer1.accounts[2].withdraw(2000, "Sushi restaurant 1")
customer1.accounts[2].withdraw(3000, "Sushi restaurant 2")


for account in customer1.accounts:
    account.print_transactions()