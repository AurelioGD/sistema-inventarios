import sqlite3
from sqlite3 import Error
from sqlStatements.databaseSqlStatements import createTableProductsSql, createTableFinancesSql

class Connection:
    def __init__(self):
        try: 
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
        except Error:
            print("Hay un error en la bd")
    def __commitConnection(self):
        self.connection.commit()
    def getConnection(self):
        return self.connection
    def getCursor(self):
        return self.cursor
    def createDatabaseStructure(self):
        self.cursor.execute(createTableProductsSql)
        self.cursor.execute(createTableFinancesSql)
        self.__commitConnection()