#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

#create login form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

#form_ok is true if the correct login info was provided
form_ok = username == secret.username and password == secret.password

#set up cookie
cookie = SimpleCookie(os.environ['HTTP_COOKIE'])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

#check if cookie username and password are correct
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

#if correct, then set the actual username and password to the cookie
if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content_Type: text/html")
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

"""#load login page and print user info if available
if not username and not password:
    print(login_page())
else:
    print(login_page())
    print("username:", username)
    print("password:", password)"""

#load login page and show secret page if correct info. otherwise show incorrect login page
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())


