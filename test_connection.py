import psycopg2

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="company_db",   
        user="postgres",       
        password="123",        
        host="localhost",
        port="5432"
    )

    print("Database connection successful!")

    # Optional: check PostgreSQL version
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("PostgreSQL version:", record)

    # Close everything
    cur.close()
    conn.close()

except Exception as e:
    print("❌ Database connection failed!")
    print("Error:", e)
