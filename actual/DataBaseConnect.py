import mysql.connector
import mysql

def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="ebmp"
    )
    mycursor = mydb.cursor()
    return mydb,mycursor