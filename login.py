#!/usr/local/bin/python
import MySQLdb
import cgi

db = MySQLdb.connect('localhost','root','ydz92xee','schema')
query = db.cursor()

def header(title):
    print "Content-type: text/html\n"
    print "<HTML>\n<HEAD>\n<TITLE>%s</TITLE>\n</HEAD>\n<BODY>\n" % (title)

def footer():
    print "</BODY></HTML>"

form = cgi.FieldStorage()
#username = query.execute("SELECT * FROM `schema` WHERE `username`='" + username + "'")
password = query.execute("SELECT * FROM `schema` WHERE `username`='" + password + "'")

if not form:
    header("Login Response")
elif form.has_key("login") and form["login"].value != "" and form.has_key("username") and form["username"].value == username:
    header("Connected ...")
    print "<center><hr><H3>Welcome back," , form["login"].value, ".</H3><hr></center>"
    print r"""<form><input type="hidden" name="session" value="%s"></form>""" % (form["login"].value)
    print "<H3><a href=http://ast-it.dk>Click here to start browsing</a></H3>"

else:
    header("No success!")
    print "<H3>Please go back and enter a valid login.</H3>"

if not form:
    header("Login Response")
elif form.has_key("login") and form["login"].value != "" and form.has_key("password") and form["password"].value == password:
    header("Connected ...")
    print "<center><hr><H3>Welcome back," , form["login"].value, ".</H3><hr></center>"
    print r"""<form><input type="hidden" name="session" value="%s"></form>""" % (form["login"].value)
    print "<H3><a href=http://ast-it.dk>Click here to start browsing</a></H3>"

else:
    header("No success!")
    print "<H3>Please go back and enter a valid login.</H3>"

footer()