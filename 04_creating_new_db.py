import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='samu123')
cur=conn.cursor()
try:
    #creating new database
    cur.execute("create database dbpy")
    dbs=cur.execute("show databases")
except:
    conn.rollback()
for x in cur:
    print(x)
conn.close()            