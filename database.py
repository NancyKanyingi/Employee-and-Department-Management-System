import psycopg2

# === Database connection constants ===
DB_NAME = "company_db"
DB_USER = "postgres"
DB_PASSWORD = "123"  
DB_HOST = "localhost"
DB_PORT = "5432"


def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("✅ Database connection successful.")
        return conn

    except Exception as e:
        print("Error connecting to the database:")
        print(e)
        return None


def create_tables():
    """Create the departments and employees tables."""
    conn = connect_db()
    if conn is None:
        return

    try:
        cur = conn.cursor()

        # Create departments table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE NOT NULL
            );
        """)

        # Create employees table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                salary INTEGER NOT NULL,
                department_id INTEGER REFERENCES departments(id)
            );
        """)

        conn.commit()
        print("Tables created successfully.")

    except Exception as e:
        print("Error while creating tables:")
        print(e)

    finally:
        cur.close()
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    create_tables()
