import snowflake.connector
import os

# --- Snowflake Connection ---
# It's recommended to use environment variables for connection details
SNOWFLAKE_USER = os.environ.get('SNOWFLAKE_USER', 'your_snowflake_user')
SNOWFLAKE_PASSWORD = os.environ.get('SNOWFLAKE_PASSWORD', 'your_snowflake_password')
SNOWFLAKE_ACCOUNT = os.environ.get('SNOWFLAKE_ACCOUNT', 'your_snowflake_account')
SNOWFLAKE_WAREHOUSE = os.environ.get('SNOWFLAKE_WAREHOUSE', 'your_snowflake_warehouse')
SNOWFLAKE_DATABASE = os.environ.get('SNOWFLAKE_DATABASE', 'your_snowflake_database')
SNOWFLAKE_SCHEMA = os.environ.get('SNOWFLAKE_SCHEMA', 'your_snowflake_schema')

def get_snowflake_data():
    """
    Connects to Snowflake and retrieves data.
    Replace 'your_table_name' with the actual table name.
    """
    conn = None
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cur = conn.cursor(snowflake.connector.cursor.DictCursor)
        # --- Replace with your actual table name ---
        cur.execute("SELECT * FROM your_table_name LIMIT 100")
        data = cur.fetchall()
        cur.close()
        return data
    except snowflake.connector.Error as e:
        return {'error': str(e)}
    finally:
        if conn is not None:
            conn.close()
