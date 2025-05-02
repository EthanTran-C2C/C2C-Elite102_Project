from database import BankDatabase

class bankingapplication:
    userInput = 0
    username = ""
    accountnumber = ""

    def __init__(self):
        self.db = BankDatabase()

    def login(self):
        self.username = input("Enter username: ")
        password = input("Enter your password: ")
        # Passed the same parameter as the functions in database
        return self.db.login(self.username, password)
    
    def createAccount(self):
        self.accountnumber = self.db.createAccount(self.username)
        print("Account" + self.accountnumber + " has been created")

    def displayMenu(self):
        print("Hello, and welcome to the Banking Application")
        print("Here is a list of options to choose from ")
        print("1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Create an account")
        print("5: Create a user")
        print("6: Close an account")
        print("7: Modify user information")
        print("8: Exit")
        user_input = input("Please select an option from the menu: ")
        self.userInput = int(user_input)

    # def check_balance(self):

    def deposit(self):
        accountNumber = int(input("What is the account number? "))
        depositAmount = float(input("Enter the amount being deposited: "))
        self.db.deposit(accountNumber, depositAmount)
        print("$" + str(depositAmount) + " has been deposited into account number " + str(accountNumber))

    def withdraw(self):
        acc = input("What is the account number?")
        val = input("Enter the amount being withdrawn")

    def createUser(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        # Calls the createUser function in the BankDatabase class
        self.db.createUser(password, username)

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
        print("withdraw")

    elif app.userInput == 4:
        app.createAccount()

    elif app.userInput == 5:
        app.createUser()

    elif app.userInput == 6:
        print("close acc")
    
    elif app.userInput == 7:
        print("modify user")
    else:
        print("exit")
else:
    print("Invalid user, please try again ")


