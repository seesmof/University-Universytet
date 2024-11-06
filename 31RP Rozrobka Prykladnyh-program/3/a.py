from MySQLdb._mysql import connect
import mysql.connector

db=mysql.connector.connect(
    user='root',
    host='localhost',
    password='1313',
    database='data'
)
c=db.cursor()

c.execute('create table customer (name varchar(233), age varchar(233))')

c.execute('show tables')
print([r for r in c])

db.close()
db.close()