#!"C:\Python27\python.exe"

# Cross-Platform Character Sheet Web App
# Created by Charlie S. Norvell
# 9/11/2017

import cgitb
cgitb.enable()

import Cookie
import os
import cgi

# if a login cookie is not found, build the login page
def notLoggedInPage():
	print '''
	<html>
		<head>
			<title> Log In </title>
		</head>
		
		<body>
			<div id="signin">
			
			<form method="post" action="passCheck.py">
			
			<p>
				<label for="username"/>
				<input id="username" name="username" type="text" required="required" placeholder="Username">
			</p>
			<p>
				<label for="password"/>
				<input id="password" name="password" type="password" required="required" placeholder="Password">
			</p>
			
			<button class="button" type="submit">Sign In</button>
			</form>
			</div>
		</body>
	</html>
	'''
	
# if a login cookie is found, build a welcome page
def loggedInPage(username):
	print '''
	<html>
		<head>
			<title>Page Redirection</title>
		</head>
		
		<body>
			<header>
        		<ul style="position:fixed;">
        			<li><a href="Story.html">Story</a></li>
        			<li><a name="about" href="Story.html#about">About</a></li>
        		<ul style="float:right;list-style-type:none;">
        '''
	print '				<li><a href="profile.py?user=' + username + '">' + username + '</a></li>'
	print '''
				</ul>
				</ul>
			</header>
			
		</body>
	</html>
	'''
	
form = cgi.FieldStorage()

#if not logged in, show the login screen.
stored_cookie_string = os.environ.get('HTTP_COOKIE')

if not stored_cookie_string:
	print 'Content-type: text/html'
	print
	notLoggedInPage()
	
else:
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	
	#if the cookie is appropriate, use it
	if 'username' in cookie:
		user = cookie['username'].values
		
		print 'Content-type: text/html'
		print
		loggedInPage(user)
		
	#if the cookie is useless, show the login screen
	else:
		print 'Content-type: text/html'
		print
		notLoggedInPage()
		

