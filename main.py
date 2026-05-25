
from service import *

def menu():
    print("\n  Bank Management System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")


def main():
    load_data()

    while True:
        menu()

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                create_account()
            elif choice == 2:
                deposit_money()
            elif choice == 3:
                withdraw_money()
            elif choice == 4:
                check_balance()
            elif choice == 5:
                transaction_history()
            elif choice == 6:
                print(" Exiting...")
                break
            else:
                print(" Invalid Choice")

        except ValueError:
            print(" Please enter a number")


if __name__ == "__main__":
    main()