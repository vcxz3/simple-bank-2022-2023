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
        print(f"Client: {self.name} {self.surname} ({self.id}) {self.datetime_created}")

    def add_account(self, number, currency, balance):
        self.accounts.append(Account(number, currency, balance))
    
    def print_accounts(self):
        for account in self.accounts:
            account.status()
    
    def delete_account(self, number):
        for account in self.accounts:
            if account.number == number:
                self.accounts.remove(account)
                print(f"Konts ar numuru {number} ir dzēsts.")
                break
        else:
            print(f"Konts ar numuru {number} nav atrasts.")

    def print_transactions(self):
        print()
        print("-" * 100)
        print(f"😀 Transaction report for customer {self.name} {self.surname}")     
        for account in self.accounts:
            account.print_transactions()

# KOMANDAS UZDEVUMS 2
# Izveido Account klases 2 metodes:
# deposit (ielikt naudu kontā)
# withdrawal (izneml naudu no konta)
# padomā un piesaisti Transaction klasi ar Account klasi
# izveido metodi balance Account klasei kas izvada konsolē konta bilanci

class Account:
    def __init__(self, number, currency, balance, status = 'Active'):
        self.number = number
        self.currency = currency
        self.balance = balance
        self.account_status = status
        self.datetime_created = datetime.datetime.now()
        self.transactions = []

    def status(self):
        print(f"Account: {self.number} ({self.currency}) {self.balance} {self.account_status}")

    def show_balance(self):
        print(f"Account {self.number} has {self.balance} {self.currency}")

    def deposit(self, amount, notes):
        self.transactions.append(Transaction(amount, notes))
        self.balance += amount

    def withdraw(self, amount, notes):
        self.transactions.append(Transaction(-amount, notes))
        self.balance -= amount

    def print_transactions(self):
        print(f"🧾 Account {self.number} {self.currency}")
        if len(self.transactions) == 0:
            print("\t💸 <no transactions for this account>")
        else:
            for transaction in self.transactions:
                transaction.status()

    


# KOMANDAS UZDEVUMS 1
# Izveidot klasi Transaction (jeb darījumi)
# __init__ metode (klases konstruktors)
# status metode (izvadīs konsolē informāciju par konkrēto darījumu)


class Transaction:
    def __init__(self, amount, notes):
        self.amount = amount
        self.notes = notes
        self.datetime_created = datetime.datetime.now()
    
    def status(self):
        print(f"\t💸 {self.amount} {self.datetime_created} {self.notes}")





customer1 = Customer("Anna", "Bērziņa", "78987-65448", "annab@someemail.co")
customer1.add_account("123456789", "EUR", 200)
customer1.add_account("987654321", "USD", 100)
customer1.add_account("852145796", "JPY", 100)

customer1.accounts[0].deposit(600, "Alga par 03/2023")
customer1.accounts[0].deposit(20, "Par dāvanu")
customer1.accounts[0].withdraw(5, "Kafeinīca Gardumi")
customer1.accounts[0].withdraw(120, "Keyboardz from online shop")

customer1.accounts[1].deposit(200, "Freelance compensation 03/2023")


customer2 = Customer("Oskars", "Liepa", "654987-123456", "oskarsl@someemail.co")
customer2.add_account("741254569", "EUR", 0)

customer2.accounts[0].deposit(600, "Alga par 03/2023")

def transfer_money(account_from, account_to, amount):
    account_from.withdraw(amount, f"Transfer to {account_to.number}")
    account_to.deposit(amount, f"Transfer from {account_from.number}")    

transfer_money(customer2.accounts[0], customer1.accounts[0], 199)

customer1.print_transactions()
customer2.print_transactions()