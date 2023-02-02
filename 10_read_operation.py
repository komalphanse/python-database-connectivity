import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="samu123",database="pythondb")
cur=conn.cursor()
try:
    #reading employee data
    cur.execute("select* from customer")
    #fetching the row from cursor object
    result=cur.fetchall()

    for x in result:
        print(x)
except:
    conn.rollback()

conn.close()           