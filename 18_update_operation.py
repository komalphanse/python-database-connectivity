import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="samu123",database="pythondb")
cur=conn.cursor()
try:
    cur.execute("update customer set name='alex' where id='110'")
    conn.commit()
except:
    conn.rollback()
conn.close()            