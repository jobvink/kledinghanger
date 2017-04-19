# dns = web0108.zxcs.nl of 185.104.29.62 of 185.104.29.62
import mysql.connector
from mysql.connector import errorcode

def getMaat(barcode):
    query = ("SELECT * FROM products WHERE barcode = %s")
    cursor = cnx.cursor()
    cursor.execute(query, (barcode,))
    return cursor.next()[2]

try:
    cnx = mysql.connector.connect(user='u15256p11072_la1', password='I)68okjQ~aCa6~w2JR^27],6',
                                  host='web0108.zxcs.nl',
                                  database='u15256p11072_la1', port='3306')
    print(getMaat('1234567891234'))
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


