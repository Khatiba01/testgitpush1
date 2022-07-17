import mysql.connector as conn
db = conn.connect(host = "localhost" ,
                    user ="root" ,
                    passwd = "Mysql@123",
                    db="ineuron_worksheet")
cursor=db.cursor()
cursor.execute("insert into khatiba.ineuron values(101,'Khatiba')")
cursor.execute("select * from khatiba.ineuron")
for i in cursor.fetchall() :
    print(i)