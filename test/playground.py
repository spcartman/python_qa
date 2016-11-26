# import mysql.connector
import pymysql

conn = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    conn.close()
