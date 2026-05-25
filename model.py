# model.py

class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")


class Bank:
    def __init__(self):
        self.accounts = {}   # dictionary

    def add_account(self, account):
        if account.acc_no in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account.acc_no] = account