import psycopg2
import os

# --- PostgreSQL Connection ---
# It's recommended to use environment variables for connection details
PG_HOST = os.environ.get('PG_HOST', 'localhost')
PG_PORT = os.environ.get('PG_PORT', '5432')
PG_USER = os.environ.get('PG_USER', 'your_postgres_user')
PG_PASSWORD = os.environ.get('PG_PASSWORD', 'your_postgres_password')
PG_DB = os.environ.get('PG_DB', 'your_postgres_db')

def get_postgres_data():
    """
    Connects to a PostgreSQL database and retrieves data.
    Replace 'your_table_name' with the actual table name.
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            port=PG_PORT,
            user=PG_USER,
            password=PG_PASSWORD,
            dbname=PG_DB
        )
        cur = conn.cursor()
        # --- Replace with your actual table name ---
        cur.execute("SELECT * FROM your_table_name LIMIT 100")
        
        # Fetch all rows and column names
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        
        # Convert rows to a list of dictionaries
        data = [dict(zip(colnames, row)) for row in rows]
        
        cur.close()
        return data
    except psycopg2.Error as e:
        return {'error': str(e)}
    finally:
        if conn is not None:
            conn.close()
