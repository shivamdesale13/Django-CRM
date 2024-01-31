import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Shivam321#',

)

#prepare a cursor
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE test")
print("done db")