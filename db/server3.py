import MySQLdb as db

HOST = "web0108.zxcs.nl"
PORT = 3306
USER = "u15256p11072_la1"
PASSWORD = "I)68okjQ~aCa6~w2JR^27],6"
DB = "u15256p11072_la1"

try:
    connection = db.Connection(host=HOST, port=PORT,
                               user=USER, passwd=PASSWORD, db=DB)
    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from your_table")
    result = dbhandler.fetchall()
    for item in result:
        print item

except Exception as e:
    print e
