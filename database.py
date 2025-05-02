import mysql.connector
class BankDatabase():
    def __init__(self):
        self.connection = mysql.connector.connect(user = 'root', database = 'banking_system', password = 'password')

    def create_user(self, pin, username):
        cursor = self.connection.cursor()
        query = "INSERT INTO user(pin, user_name) VALUES (%s, %s)"
        cursor.execute(query, (pin, username,))
        self.connection.commit()
    # def deposit(self, pin):
    #     cursor = self.connection.cursor()
    #      query = " "
    #      cursor.execute(query, (pin, username,))
    #      self.connection.commit()
