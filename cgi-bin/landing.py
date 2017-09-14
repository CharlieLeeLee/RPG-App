#!"C:\Python27\python.exe"

# Cross-System RPG character sheet web app
# Created by Charlie S. Norvell
# 9/11/2017

import cgitb
cgitb.enable()


# to run if a login cookie is not found
def noCookiePage():
    print '''
    <html>
        <head>
            <title> Cross-System Character Creator </title>
        </head>

        <body>
            <meta http-equiv="refresh"
            content="0; url=index.html">
