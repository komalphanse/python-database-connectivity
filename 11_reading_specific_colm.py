import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="samu123",database="pythondb")
cur=conn.cursor()
try:
    cur.execute("select name,id,salary from customer")
    result=cur.fetchall()
    for x in result:
        print(x)
except:
    conn.rollback()
conn.close()    
