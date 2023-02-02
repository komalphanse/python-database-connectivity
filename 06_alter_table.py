import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='samu123',database='pythondb')
cur=conn.cursor()
try:
    cur.execute("alter table customer add branch_name varchar(20)not null")
except:
    conn.rollback()
conn.close()        