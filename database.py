import psycopg2
from psycopg2 import sql

DB_NAME = "company_db"
DB_USER = "postgres"
db_password = "123"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname= DB_NAME,
        user=DB_USER,       
        password=DB_PASSWORD,        
        host=DB_HOST,
        port=DB_PORT
    )

    print("Connected successfully!")

except Exception as e:
    print("Failed to connect to database:")
    print(e)
    
    cur = conn.cursor()

def create_tables():
    """Create table if they don't exist."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            salary NUMERIC(10,2),
            department_id INTEGER REFERENCES departments(id) ON DELETE SET NULL
        );
    """)
    conn.commit()
    print("Tables created successfully (departments, employees).")

    except Exception as e:
    print("Error while connecting or creating tables:")
    print(e)

    finally:
    # Always close connection
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    create_tables()