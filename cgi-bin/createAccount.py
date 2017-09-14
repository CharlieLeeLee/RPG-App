#!"C:\Python27\python.exe"

# Cross-Platform Character Sheet Web App
# Created by Charlie S. Norvell
# 9/11/2017

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

import Cookie
import os
import datetime

username = form['username'].value
password = form['password'].value

# connect and open database
import sqlite3

conn = sqlite3.connect('charSheetApp.db')
c = conn.cursor

# insert new user data into the database
c.execute('INSERT into ACCOUNTS values (?, ?)', (username, password))
conn.commit

# create a cookie for the new user
cookie = Cookie.SimpleCookie()
cookie['username'] = username

# cookie expires in 30 days
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
cookie['username']['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')

# print the http header
print 'Content-Type: text/html'
print cookie
print

# redirect page to user profile

print '''
	<html>
		<head>
			<title> Account Page </title>
		</head>
		
		<body>
		'''
print '			<meta http-equiv="refresh"'
print '				content="0; url=profile.py?username=' + username + '">'

conn.close()

print '''
		</body>
	</html>
'''