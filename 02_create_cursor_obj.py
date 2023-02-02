import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='samu123',database='komal')
print(conn)
cur=conn.cursor()
print(cur)