#Create databa
#create database nlpproj

#Use database
use nlpproj

#Create table student
"""
	Student => sId | name | sex | addrees | phone | cgpa | 
"""
CREATE TABLE student (
 sId INTEGER PRIMARY KEY,
 name VARCHAR(20) NOT NULL,
 sex CHAR(7),
 address VARCHAR(50), 
 phone CHAR(20),
 cgpa INTEGER
);


#Create table department
CREATE TABLE department (
 dId INTEGER PRIMARY KEY,
 name VARCHAR(30),
 buildingCode INTEGER
);

#Create users table
CREATE TABLES users )
	userid  VARCHAR(30) PRIMARY KEY
	password VARCHAR(30)
	access INTEGER
	name VARCHAR(30)
);
