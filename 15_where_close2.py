import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="samu123",database="pythondb")
cur=conn.cursor()
try:
    cur.execute("select name,id,salary from customer where id in (102,103,104)")
    result=cur.fetchall()
    print("name   id  salary")

    for x in result:
        print("%s %d %d"%(x[0],x[1],x[2]))
except:
    conn.rollback()
conn.close()            