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

<input type = "radio" name = "dbact" value = "drop"> DROP<br>
Database name: <input type="text" name="dbname" value="">
<br><br>


        <div>TABLES</div>
<input type ="radio" name="tbact" value="create"> CREATE<br>
<input type="radio" name="tbact" value="drop"> DROP<br>
Database name: <input type ="text" name="tbname" value="">
Table name: <input type="text" name="tbname" value="">
<br><br>

    <div>QUERIES</div>
<input type="radio" name="qact" value="select"> SELECT<br>
<input type="radio" name="quact" value="insert"> INSERT<br>
Database name: <input type ="text" name="qdbname" value="">
Table name: <input type="text" name="qtbnamee" value="">
Columns (comma-seperated) : <input type="text" name="values"
Value=""><br>

<input type="submit" value="submit">
        </form>
    </body>
</html>

footer()