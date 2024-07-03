import pymysql
import sys

conn = pymysql.connect(host="localhost",user="root",password="rps@123",db="demodb_1")

if not conn:
    sys.exit(0)

try:
    cur = conn.cursor()
    cur.execute("select emp_no,first_name,last_name from employee")
except pymysql.Error as e:
    print(e)
else:
    records = cur.fetchall()
    for rec in records:
        #print(f"Number:{rec[0]},Fname:{rec[1]},Lname{rec[2]}")
        print(f"Number:{rec['emp_no']},Fname:{rec['first_name']},Lname{rec['last_name']}")
finally:
    conn.close()