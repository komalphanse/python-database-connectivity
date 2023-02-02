import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="samu123",database="pythondb")
cur=conn.cursor()
sql="insert into department(dept_id,dept_name)values(%s,%s)"
val=[(205,"CS"),(202,"IT"),(203,"BE")]
try:
    cur.executemany(sql,val)
    conn.commit()

except:
    conn.rollback() 
print(cur.rowcount,"record inserted")

conn.close()   