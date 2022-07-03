import mysql.connector as connector
import MySQLdb

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host= 'localhost',
                                port='3306',
                                user='root',
                                password='1234',
                                database='purva_db')
    def create_db(self):
        query="create database if not exists purva_db"
        cur= self.con.cursor()
        cur.execute(query)

    def create_table(self):
        query="create table if not exists employee(empid int, name varchar(50))"
        cur= self.con.cursor()
        cur.execute(query)

if __name__ == '__main__':
    obj1 = DBhelper()
#    obj1.create_db()
    obj1.create_table()
