import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="samu123",database="pythondb")
cur=conn.cursor()
sql="insert into customer(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=("john",110,25000,201,"newyork")
try:
    cur.execute(sql,val)
    conn.commit()
except:
    conn.rollback() 
print(cur.rowcount,"record inserted")
conn.close()   