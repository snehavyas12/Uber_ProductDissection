import psycopg2
from psycopg2 import sql, OperationalError, Error

HOST="database-1.cyny6g844cq5.us-east-1.rds.amazonaws.com"
PORT=5432
ADMIN_USER="postgres"
ADMIN_PASSWORD="Batuktingu"

NEW_DB_NAME = "uber_db"   
ENCODING = "UTF8"


#create a maintainence connection to the default 'postgres' database
'''
because, CREATE DATABASE cannot be run inside the database you're about to create — 
you connect to an existing DB (like postgres) and issue CREATE DATABASE. 
sslmode="require" enforces SSL/TLS between client and RDS — good security practice (RDS often requires SSL). 
Using a single function reduces duplication and centralizes connection logic.
'''

def get_connected_default_db():
    # Connect to the default database (postgres) as admin
    print(f"HOST={HOST}, PORT={PORT}, ADMIN_USER={ADMIN_USER}, ADMIN_PASSWORD={ADMIN_PASSWORD}")
    return psycopg2.connect(
        host=HOST,
        port=PORT,
        user=ADMIN_USER,
        password=ADMIN_PASSWORD,
        dbname="postgres",   # maintenance DB
        sslmode="require"    # enforced if RDS requires SSL
    )

'''
As we are creating a new database, we will first check if the a database of same name exists already.
'''
def check_database_exists(connection, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s;"),
            [db_name]
        )
        return cursor.fetchone() is not None
    except Error as e:
        print(f"Error checking database existence: {e}")
        return False
    finally:
        cursor.close()

def create_database():
    conn = None
    try:
        conn = get_connected_default_db()
        conn.autocommit = True  # required for CREATE DATABASE outside transactions
        if check_database_exists(conn, NEW_DB_NAME):
            print(f"Database {NEW_DB_NAME} already exists.")
            return
        else:
            print(f"Database {NEW_DB_NAME} does not exist.")
        with conn.cursor() as cur:
            # Example: set owner to admin user. Adjust if you want a different owner.
            cur.execute(
                sql.SQL("CREATE DATABASE {} WITH OWNER = %s ENCODING = %s;")
                   .format(sql.Identifier(NEW_DB_NAME)),
                (ADMIN_USER, ENCODING)
            )
        print(f"Database {NEW_DB_NAME} created.")
    except OperationalError as e:
        print("OperationalError:", e)
        raise
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database()

    
    