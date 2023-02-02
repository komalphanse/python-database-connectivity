import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='samu123',database='pythondb')
cur=conn.cursor()

cur.execute("create table department(dept_id int(20) not null primary key,dept_name varchar(20) not null)")

conn.close()        