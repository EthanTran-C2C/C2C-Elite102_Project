import mysql.connector
class BankDatabase():
    # Creates the connection to the database
    def __init__(self):
        self.connection = mysql.connector.connect(user = 'root', database = 'banking_system', password = 'password')
    # Allows the user to login to their account. Returns true if the user entered their username and password correctly, and false otherwise
    def login(self, username, password):
        # Returns true if the user is in the database based on the provided username and password
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM user WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result[0] == 1:
            return True
        else:
            return False  
        cursor.close() 
    # Fetches the account number from the user, to be used in other functions
    def getAccountNumber(self, username):
        cursor = self.connection.cursor()
        query = "SELECT account_number FROM user WHERE user_name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    # Creates the users account by adding a new row into the accounts table of the SQL database
    def createAccount(self, username):
        cursor = self.connection.cursor()
        query = "INSERT INTO account(balance, status) VALUES (0.00, 'OPEN')"
        cursor.execute(query)
        # Get the account_number of the newly inserted account
        account_number = cursor.lastrowid
        query = "UPDATE user SET account_number = %s WHERE user_name = %s"
        cursor.execute(query, (account_number, username))
        self.connection.commit()
        cursor.close()
        return account_number
    # Creates a new user, with a new username and passwor that is added to the user SQL database
    def createUser(self, password, username):
        # Establishes the cursor, an object that allows interaction with database
        cursor = self.connection.cursor()
        # sql code
        query = "INSERT INTO user(password, user_name) VALUES (%s, %s)"
        cursor.execute(query, (password, username))
        self.connection.commit()
        cursor.close()
    # Adds money to the account balance
    def deposit(self, accountNumber, depositAmount):
        cursor = self.connection.cursor()
        query = "UPDATE ACCOUNT SET BALANCE = BALANCE + %s WHERE ACCOUNT_NUMBER = %s"
        cursor.execute(query, (depositAmount, accountNumber))
        self.connection.commit()
        cursor.close()
    # Removes money from the account balance
    def withdraw(self, accountNumber, withdrawAmount):
        cursor = self.connection.cursor()
        query = "UPDATE ACCOUNT SET BALANCE = BALANCE - %s WHERE ACCOUNT_NUMBER = %s"
        cursor.execute(query, (withdrawAmount, accountNumber))
        self.connection.commit()
        cursor.close()
    # Returns the account balance where the the account number is the users account number
    def checkBalance(self, accountNumber):
        cursor = self.connection.cursor()
        query = 'SELECT balance FROM account WHERE account_number = %s'
        cursor.execute(query, (accountNumber,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    # Updates the status of the users current account to closed
    def closeAccount(self, accountNumber):
        cursor = self.connection.cursor()
        query = 'UPDATE account SET status = "CLOSED" WHERE account_number = %s'
        cursor.execute(query, (accountNumber,))
        self.connection.commit()
        cursor.close()
    # Changes the users password
    def modifyAccount(self, password, username):
        cursor = self.connection.cursor()
        # Query contains SQL commands
        query = 'UPDATE USER SET password = %s WHERE user_name = %s'
        # Executing the SQL commands with parameters
        cursor.execute(query, (password, username))
        # Any changes made to the SQL tabes are comitted
        self.connection.commit()
        # Cursor closed after accessing the SQL tables to prevent errors
        cursor.close()
    
