import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="samu123",database="pythondb")
cur=conn.cursor()
sql="insert into customer(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=[("Joseph",102,25000,205,"newyork"),("David",103,25000,202,"port of spain"),("Nick",104,20000,203,"germoni")]
try:
    cur.executemany(sql,val)
    conn.commit()

except:
    conn.rollback() 
print(cur.rowcount,"record inserted")

conn.close()   