import mysql.connector
class BankDatabase():
    def __init__(self):
        self.connection = mysql.connector.connect(user = 'root', database = 'banking_system', password = 'password')

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
    
    def getAccountNumber(self, username):
        cursor = self.connection.cursor()
        query = "SELECT account_number FROM user WHERE user_name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
        
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

    def createUser(self, password, username):
        # Establishes the cursor, an object that allows interaction with database
        cursor = self.connection.cursor()
        # sql code
        query = "INSERT INTO user(password, user_name) VALUES (%s, %s)"
        cursor.execute(query, (password, username))
        self.connection.commit()
        cursor.close()

    def deposit(self, accountNumber, depositAmount):
        cursor = self.connection.cursor()
        query = "UPDATE ACCOUNT SET BALANCE = BALANCE + %s WHERE ACCOUNT_NUMBER = %s"
        cursor.execute(query, (depositAmount, accountNumber))
        self.connection.commit()
        cursor.close()

    def withdraw(self, accountNumber, withdrawAmount):
        cursor = self.connection.cursor()
        query = "UPDATE ACCOUNT SET BALANCE = BALANCE - %s WHERE ACCOUNT_NUMBER = %s"
        cursor.execute(query, (withdrawAmount, accountNumber))
        self.connection.commit()
        cursor.close()

    def checkBalance(self, accountNumber):
        cursor = self.connection.cursor()
        query = 'SELECT balance FROM account WHERE account_number = %s'
        cursor.execute(query, (accountNumber,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    
    
