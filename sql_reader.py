from sqlalchemy import create_engine, text
import os

# --- Generic SQL Connection using SQLAlchemy ---
# The connection string can be configured for different SQL databases (e.g., SQLite, MySQL, etc.)
# It's recommended to use environment variables for the connection string.
# Example for SQLite: 'sqlite:///your_database.db'
# Example for MySQL: 'mysql+mysqlconnector://user:password@host/dbname'
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL', 'sqlite:///your_database.db')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_sql_data():
    """
    Connects to a SQL database using SQLAlchemy and retrieves data.
    Replace 'your_table_name' with the actual table name.
    """
    with engine.connect() as connection:
        try:
            # --- Replace with your actual table name ---
            query = text("SELECT * FROM your_table_name LIMIT 100")
            result = connection.execute(query)
            
            # Fetch all rows and column names
            rows = result.fetchall()
            colnames = result.keys()
            
            # Convert rows to a list of dictionaries
            data = [dict(zip(colnames, row)) for row in rows]
            return data
        except Exception as e:
            return {'error': str(e)}
