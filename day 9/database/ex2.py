import pymysql
import sys

conn = pymysql.connect(host="localhost",user="root",password="rps@123",db="demodb_1")

if not conn:
    sys.exit(0)

try:
    cur = conn.cursor()
    cur.execute("insert into employee values(10015,'1958-02-19','Bob','Smith','M','1994-09-15',6000,'d006')")
    conn.commit()
except pymysql.Error as e:
    print(e)
else:
    records = cur.fetchall()
    for rec in records:
        print(f"Number:{rec[0]},Fname:{rec[1]},Lname{rec[2]}")
finally:
    conn.close()