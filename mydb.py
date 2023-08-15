import mysql.connector

dataBase = mysql.connector.connect(
	host = '%',
	user = 'try',
	passwd = '7*5*3*1*5*9'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")