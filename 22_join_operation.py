import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="samu123",database="pythondb")
cur=conn.cursor()

try:
    cur.execute("select customer.id,customer.name,customer.salary,department.dept_id,department.dept_name from department join customer on department.dept_id=customer.dept_id")
    print("id name  salary dept_id dept_name")
    for x in cur:
        print("%d %s %d %d %s"%(x[0],x[1],x[2],x[3],x[4]))

except:
    conn.rollback() 


conn.close()   