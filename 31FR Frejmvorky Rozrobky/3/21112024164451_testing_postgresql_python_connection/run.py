import psycopg2

db=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='1414',
    host='localhost',
    port=5432,
)
