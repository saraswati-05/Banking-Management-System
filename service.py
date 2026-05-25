
import os
from model import Account, Bank

DATA_FILE = "data.txt"

bank = Bank()


def save_data():
    with open(DATA_FILE, "w") as f:
        for acc in bank.accounts.values():
            line = f"{acc.acc_no},{acc.name},{acc.balance}\n"
            f.write(line)


def load_data():
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, "r") as f:
        for line in f:
            acc_no, name, balance = line.strip().split(",")
            account = Account(int(acc_no), name, float(balance))
            bank.accounts[int(acc_no)] = account


def create_account():
    try:
        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ").strip()

        if not name:
            print(" Name cannot be empty")
            return

        account = Account(acc_no, name)
        bank.add_account(account)

        save_data()
        print(" Account Created Successfully")

    except ValueError as e:
        print(" Error:", e)


def deposit_money():
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        account = bank.accounts.get(acc_no)
        if not account:
            print("Account Not Found")
            return

        account.deposit(amount)
        save_data()
        print(" Amount Deposited")

    except ValueError:
        print(" Invalid Input")


def withdraw_money():
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        account = bank.accounts.get(acc_no)
        if not account:
            print(" Account Not Found")
            return

        account.withdraw(amount)
        save_data()
        print(" Amount Withdrawn")

    except ValueError as e:
        print( e)


def check_balance():
    try:
        acc_no = int(input("Enter Account Number: "))
        account = bank.accounts.get(acc_no)

        if not account:
            print(" Account Not Found")
            return

        print(f" Balance: {account.balance}")

    except ValueError:
        print(" Invalid Input")


def transaction_history():
    try:
        acc_no = int(input("Enter Account Number: "))
        account = bank.accounts.get(acc_no)

        if not account:
            print(" Account Not Found")
            return

        print("Transaction History:")
        for t in account.transactions:
            print(t)

    except ValueError:
        print(" Invalid Input")