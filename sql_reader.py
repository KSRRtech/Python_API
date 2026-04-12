from sqlalchemy import create_engine, text
import os

# --- Generic SQL Connection using SQLAlchemy ---
# The connection string can be configured for different SQL databases (e.g., SQLite, MySQL, etc.)
# It's recommended to use environment variables for the connection string.
# Example for SQLite: 'sqlite:///your_database.db'
# Example for MySQL: 'mysql+mysqlconnector://user:password@host/dbname'
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL', 'sqlite:///your_database.db')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_sql_data(table_name: str, limit: int = 100) -> list | dict:
    """
    Connects to a SQL database using SQLAlchemy and retrieves data.
    
    Args:
        table_name: The name of the table to query
        limit: Maximum number of rows to retrieve (default: 100)
    
    Returns:
        List of dictionaries containing row data, or dict with error
    """
    if not table_name or not table_name.replace('_', '').isalnum():
        return {'error': 'Invalid table name'}
    
    try:
        with engine.connect() as connection:
            query = text(f"SELECT * FROM {table_name} LIMIT :limit")
            result = connection.execute(query, {"limit": limit})
            
            # Convert rows to list of dictionaries
            return [dict(row._mapping) for row in result]
    except Exception as e:
        print(f"Error querying table '{table_name}': {str(e)}")
        return {'error': str(e)}
