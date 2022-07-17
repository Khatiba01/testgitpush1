import mysql.connector as conn
db = conn.connect(host = "localhost" ,
                    user ="root" ,
                    passwd = "Mysql@123",
                    db="ineuron_worksheet")
cursor=db.cursor()
print(mydb)
s="create table if not exists khatiba.ineuron(emp_id int(10),emp_name varchar(80))"

q1=cursor.execute(s)
q2=cursor.execute("select * from khatiba.ineuron")
print(q2)