import mysql.connector
class BankDatabase():
    def __init__(self):
        self.connection = mysql.connector.connect(user = 'root', database = 'banking_system', password = 'password')

    def createUser(self, pin, username):
        cursor = self.connection.cursor()
        query = "INSERT INTO user(pin, user_name) VALUES (%s, %s)"
        cursor.execute(query, (pin, username,))
        self.connection.commit()
    def deposit(self, accountNumber, depositAmount):
        cursor = self.connection.cursor()
        query = "UPDATE ACCOUNT SET BALANCE = BALANCE + %s WHERE ACCOUNT_NUMBER = %s"
        cursor.execute(query, (accountNumber, username))
        self.connection.commit()
