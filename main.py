import unittest
from database import BankDatabase
from tkinter import *
from tkinter import ttk

class bankingapplilcation:
    def __init__(self):
        self.db = BankDatabase()
    def ui():
        print("Hello, and welcome to the Banking Application")
        print("Here is a list of options to choose from ")
        print("1: Cash a check")
        print("2: Deposit or withdraw funds")
        print("3: Register or delete an account")
        print("4: Modify account information")
        user_input = input("Please select an option from the menu:")

    # def check_balance():

    def deposit(self):
        acc = input("What is the account number?")
        val = input("Enter how much money")
    # def withdraw():
    
    def create_user(self):
        username = input("Enter a username: ")
        pin = input("Enter a PIN: ")
        self.db.create_user(pin, username)

    # def close_account():

    # def modify_account():

app = bankingapplilcation()
app.create_user()