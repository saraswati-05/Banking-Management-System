# Banking Management System

## Project Overview

The Banking Management System is a console-based application developed using Python.  
This project is designed to perform basic banking operations such as account creation, deposit, withdrawal, balance enquiry, and transaction history management.

The system uses Object-Oriented Programming concepts and file handling techniques to store customer account details permanently.

---

# Features

- Create New Bank Account
- Deposit Money into Existing Account
- Withdraw Money from Account
- Check Account Balance
- View Transaction History
- Persistent Data Storage using File Handling
- Exception Handling for Invalid Inputs
- Menu-Driven User Interface

---

# Technologies Used

- Python
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- VS Code

---

# Project Structure

```text
Banking-Management-System/
│
├── main.py
├── service.py
├── model.py
├── data.txt
└── README.md
```

---

# Modules Description

## 1. main.py
Handles the main menu and user interaction.

## 2. service.py
Contains all banking operations such as:
- Create Account
- Deposit Money
- Withdraw Money
- Check Balance
- Transaction History

## 3. model.py
Contains classes:
- Account Class
- Bank Class

## 4. data.txt
Stores account details permanently using file handling.

---

# Functionalities

## Account Creation
Allows users to create a new bank account using account number and customer name.

## Deposit Money
Users can deposit money into their account and the balance updates automatically.

## Withdraw Money
Users can withdraw money if sufficient balance is available.

## Balance Enquiry
Displays the current account balance.

## Transaction History
Stores and displays all deposits and withdrawals.

---

# Concepts Used

- Classes and Objects
- Functions
- Dictionary
- File Handling
- Exception Handling

---

# How to Run the Project

## Step 1: Clone Repository

```bash
git clone https://github.com/saraswati-05/Banking-Management-System.git
```

## Step 2: Open Project Folder

```bash
cd Banking-Management-System
```

## Step 3: Run Project

```bash
python main.py
```

---

# Sample Output

```text
🏦 Bank Management System
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Exit
```

---

# Advantages

- Easy to use
- Beginner-friendly project
- Real-world banking simulation
- Permanent data storage
- Good understanding of Python concepts

---

# Future Enhancements

- Login Authentication
- GUI Interface using Tkinter
- Database Integration using MySQL
- Money Transfer Feature
- ATM PIN Security

---

# Author

Saraswati Sonale
