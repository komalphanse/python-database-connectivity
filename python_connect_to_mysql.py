import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='samu123',database='komal')
my_cursor=conn.cursor()
conn.close()
print("connection successfully created")