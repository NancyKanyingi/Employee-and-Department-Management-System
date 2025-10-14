import psycopg2

# Connect to PostgreSQL

def get_connection():
    return psycopg2.connect(
        host = "local host",
        dbname = "company_db",
        user = "company_user",
        password = "123"
        port = "5432"
    )

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
    cur.close()
    conn.close()