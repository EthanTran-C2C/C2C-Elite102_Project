import unittest
from database import BankDatabase
from tkinter import *
from tkinter import ttk

class bankingapplication:
    userInput = 0
    username = ""
    accountnumber = ""

    def __init__(self):
        self.db = BankDatabase()

    def login(self):
        self.username = input("Enter username: ")
        password = input("Enter your pin: ")
        # Passed the same parameter as the functions in database
        return self.db.login(self.username, password)

    def displayMenu(self):
        print("Hello, and welcome to the Banking Application")
        print("Here is a list of options to choose from ")
        print("1: Check Balance")
        print("2: Deposit or withdraw funds")
        print("3: Register an account")
        print("4: Close an account")
        print("5: Modify account information")
        print("6: Exit")
        user_input = input("Please select an option from the menu: ")
        self.userInput = int(user_input)

    # def check_balance(self):

    def deposit(self):
        accountNumber = int(input("What is the account number? "))
        depositAmount = float(input("Enter the amount being deposited: "))
        self.db.deposit(accountNumber, depositAmount)
        print("$" + str(depositAmount) + " has been deposited into account number " + str(accountNumber))

    def withdraw():
        acc = input("What is the account number?")
        val = input("Enter the amount being withdrawn")

    def createUser(self):
        username = input("Enter a username: ")
        pin = input("Enter a PIN: ")
        # Calls the createUser function in the BankDatabase class
        self.db.createUser(pin, username)

    # def close_account():
        
    # def modify_account():

app = bankingapplication()
if app.login():
    app.displayMenu()

    if app.userInput == 1:
        print("check balance here")

    elif app.userInput == 2:
        app.deposit()

    elif app.userInput == 3:
        app.createUser()

    elif app.userInput == 4:
        print("Close acc")

    elif app.userInput == 5:
        print("Mod acc")
            
    else:
        print("exit")
else:
    print("Invalid user, please try again ")


