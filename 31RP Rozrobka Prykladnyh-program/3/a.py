from MySQLdb._mysql import connect
import mysql.connector

db=connect(
    host='localhost',
    user='root',
    password='1313',
)
print(db)