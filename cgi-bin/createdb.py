#!"C:\Python27\python.exe"

# Cross-Platform Character Sheet Web App
# Created by Charlie S. Norvell
# 9/11/2017

import sqlite3

# Create a database file called 'charSheetApp.db' if it doesn't exist yet.
# if this file already exists, the program will quit.

conn = sqlite3.connect('charSheetApp.db')
c = conn.cursor()

# Create a new 'USERS' table with 2 columns: username, password
c.execute('create table USERS(username varchar(50) primary key, password varchar(100)')

# Create a new 'CHARACTERS' table with 5 columns: id, owner, charName, system, json
c.execute('''create table CHARACTERS
			(id real primary key, owner varchar(50), charName varchar(100), system varChar(20), json text)''')

# commit and close
conn.commit()
conn.close()