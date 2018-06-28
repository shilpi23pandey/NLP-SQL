from flask import Flask
from flaskext.mysql import MySQL
mysql = MySQL()


#print('Successful connection')
cursor = mysql.get_db().cursor()

def executeQuery(sqlQuery):
	cursor.execute(sqlQuery)
	return cursor.fetchall()
