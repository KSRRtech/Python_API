from databricks import sql
import os

# --- Databricks Connection ---
# It's recommended to use environment variables for connection details
DATABRICKS_SERVER_HOSTNAME = os.environ.get('DATABRICKS_SERVER_HOSTNAME', 'your_databricks_hostname')
DATABRICKS_HTTP_PATH = os.environ.get('DATABRICKS_HTTP_PATH', 'your_databricks_http_path')
DATABRICKS_ACCESS_TOKEN = os.environ.get('DATABRICKS_ACCESS_TOKEN', 'your_databricks_token')

def get_databricks_data():
    """
    Connects to Databricks SQL and retrieves data.
    Replace 'your_table_name' with the actual table name.
    """
    connection = None
    try:
        connection = sql.connect(
            server_hostname=DATABRICKS_SERVER_HOSTNAME,
            http_path=DATABRICKS_HTTP_PATH,
            access_token=DATABRICKS_ACCESS_TOKEN
        )
        cursor = connection.cursor()
        # --- Replace with your actual table name ---
        cursor.execute("SELECT * FROM your_table_name LIMIT 100")
        
        # Fetch all rows and column names
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        
        # Convert rows to a list of dictionaries
        data = [dict(zip(colnames, row)) for row in rows]
        
        cursor.close()
        return data
    except Exception as e:
        return {'error': str(e)}
    finally:
        if connection is not None:
            connection.close()
