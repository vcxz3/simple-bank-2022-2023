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


class Account:
    def __init__(self, number, currency, balance, account_status = 'Active'):
        self.number = number
        self.currency = currency
        self.balance = balance
        self.datetime_created = datetime.datetime.now()
        self.account_status = account_status

    def status(self):
        print(f"Account: {self.number} ({self.currency}) {self.balance}")


customer1 = Customer("Anna", "Bērziņa", "123456-789456", "annab@someemail.com")
customer1.add_account("123456789", "EUR", 200)
customer1.add_account("321654987", "USD", 100)
customer1.add_account("8521236575", "JPY", 15000)

customer1.status()
customer1.print_accounts()

customer1.delete_account("321654988")
customer1.print_accounts()