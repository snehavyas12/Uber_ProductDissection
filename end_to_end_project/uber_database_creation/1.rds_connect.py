import psycopg2

conn = psycopg2.connect(
    host = 'database-1.cyny6g844cq5.us-east-1.rds.amazonaws.com',
    database = 'postgres',
    user = 'postgres',
    password = 'Batuktingu',
    port = '5432'
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record, "\n")