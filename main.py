# Copyright Stig Haag Brommann Ast-it.dk
# Made for Year-project 2015 at Øse Efterskole
import MySQLdb

print ("Velkommen til mit log ind script!")
db = MySQLdb.connect(host = "localhost",
                     user = "root",
                     passwd = "ydz92xee",
                     db = "schema")

query = db.cursor()

loop = 'true'
while(loop == 'true'):
    username = input("Username : ")
    password = input("Password : ")
    if(query.execute("SELECT * FROM `USERS` WHERE `username`='" + username +  "' AND `password`='" + password + "'")):
        db.commit()
        print ("Du er nu logget ind!")
        break
    else:
        db.commit()
        print ("Login fejlede!")
