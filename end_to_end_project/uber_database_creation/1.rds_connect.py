import psycopg2

conn = psycopg2.connect(
    host = '<endpoint>',
    database = '<db_name>',
    user = 'postgres',
    password = '<password>',
    port = '5432'
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record, "\n")