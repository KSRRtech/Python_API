from fastapi import FastAPI
from database import get_all_data
from postgres_reader import get_postgres_data
from snowflake_reader import get_snowflake_data
from databricks_reader import get_databricks_data
from sql_reader import get_sql_data

# Create a FastAPI application
app = FastAPI()

@app.get('/data/mongo')
def get_mongo_data_endpoint():
    """
    This endpoint retrieves all documents from the MongoDB collection.
    """
    return get_all_data()

@app.get('/data/postgres')
def get_postgres_data_endpoint():
    """
    This endpoint retrieves data from the PostgreSQL database.
    """
    return get_postgres_data()

@app.get('/data/snowflake')
def get_snowflake_data_endpoint():
    """
    This endpoint retrieves data from Snowflake.
    """
    return get_snowflake_data()

@app.get('/data/databricks')
def get_databricks_data_endpoint():
    """
    This endpoint retrieves data from Databricks.
    """
    return get_databricks_data()

@app.get('/data/sql')
def get_sql_data_endpoint():
    """
    This endpoint retrieves data from a generic SQL database using SQLAlchemy.
    """
    return get_sql_data()

