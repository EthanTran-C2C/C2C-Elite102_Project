from database import BankDatabase

class bankingapplication:
    userInput = 0
    username = ""
    accountNumber = 0
    # Creates an instance of the bankdatabase
    def __init__(self):
        self.db = BankDatabase()
    # The user logs in using their username and password. Once in, they can then access their account or create one
    def login(self):
        self.username = input("Enter username: ")
        password = input("Enter your password: ")
        # Passed the same parameter as the functions in database
        validUser = self.db.login(self.username, password)
        if validUser:
            self.accountNumber = self.db.getAccountNumber(self.username)
        return validUser
    # Allows the user, once signed in, to create an account
    def createAccount(self):
        self.accountNumber = self.db.createAccount(self.username)
        print("Account " + str(self.accountNumber) + " has been created")
    #Displays the menu of options that the user can choose from
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
    # Returns the current balance in the account
    def check_balance(self):
        balance = self.db.checkBalance(self.accountNumber)
        print("The balance is $" + str(balance))
    # The user enters an amount of money, which is then added into their account balance
    def deposit(self):
        #accountNumber = int(input("What is the account number? "))
        depositAmount = float(input("Enter the amount being deposited: "))
        self.db.deposit(self.accountNumber, depositAmount)
        print("$" + str(depositAmount) + " has been deposited into account number " + str(self.accountNumber))
    # The user enters an amount of money, which is then removed from their account balance
    def withdraw(self):
        #acc = int(input("What is the account number?"))
        withdrawAmount = float(input("Enter the amount being withdrawn: "))
        self.db.withdraw(self.accountNumber, withdrawAmount)
        self.check_balance()
    # Creates a user account, with its own username and password. Limited by the fact that their must already by a user to create a user
    def createUser(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        # Calls the createUser function in the BankDatabase class
        self.db.createUser(password, username)
    # Deletes the users account. User can then create another account
    def close_account(self):
        self.db.closeAccount(self.accountNumber)
        print(str(self.accountNumber) + " has been closed!")
    # Changes the users password
    def modifyAccount(self):
        password = input("Enter a new password: ")
        self.db.modifyAccount(password, self.username)

app = bankingapplication()
# Displays the menu of options if the user sucessfully enters a username and password
if app.login():
    app.displayMenu()

    if app.userInput == 1:
        app.check_balance()

    elif app.userInput == 2:
        app.deposit()

    elif app.userInput == 3:
        app.withdraw()

    elif app.userInput == 4:
        app.createAccount()

    elif app.userInput == 5:
        app.createUser()

    elif app.userInput == 6:
        app.close_account()
    
    elif app.userInput == 7:
        app.modifyAccount()
    else:
        print("Thank you for using the application")
else:
    print("Invalid user, please try again ")


