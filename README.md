# Python Multi-Source Data API

This project is a Python API built with FastAPI to read data from multiple sources: MongoDB, PostgreSQL, Snowflake, Databricks, and any SQL database supported by SQLAlchemy.

## Setup

1.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**

    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your data sources:**

    It is highly recommended to configure your connection settings using environment variables.

    *   **MongoDB (`database.py`):**
        - Replace `'your_database_name'` and `'your_collection_name'` with your actual database and collection names.

    *   **PostgreSQL (`postgres_reader.py`):**
        - `PG_HOST`: The database host.
        - `PG_PORT`: The database port.
        - `PG_USER`: Your PostgreSQL username.
        - `PG_PASSWORD`: Your PostgreSQL password.
        - `PG_DB`: The name of the database.
        - Replace `'your_table_name'` with the table you want to query.

    *   **Snowflake (`snowflake_reader.py`):**
        - `SNOWFLAKE_USER`: Your Snowflake username.
        - `SNOWFLAKE_PASSWORD`: Your Snowflake password.
        - `SNOWFLAKE_ACCOUNT`: Your Snowflake account identifier.
        - `SNOWFLAKE_WAREHOUSE`: The warehouse to use.
        - `SNOWFLAKE_DATABASE`: The database to use.
        - `SNOWFLAKE_SCHEMA`: The schema to use.
        - Replace `'your_table_name'` with the table you want to query.

    *   **Databricks (`databricks_reader.py`):**
        - `DATABRICKS_SERVER_HOSTNAME`: Your Databricks workspace URL.
        - `DATABRICKS_HTTP_PATH`: The HTTP path of your Databricks SQL endpoint.
        - `DATABRICKS_ACCESS_TOKEN`: Your Databricks personal access token.
        - Replace `'your_table_name'` with the table you want to query.

    *   **Generic SQL (`sql_reader.py`):**
        - `SQLALCHEMY_DATABASE_URL`: The SQLAlchemy connection string for your database.
        - Replace `'your_table_name'` with the table you want to query.

## Running the API

1.  **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

2.  **Access the API:**

    The API will be running at `http://127.0.0.1:8000`. You can access the following endpoints:

    *   `/data/mongo`
    *   `/data/postgres`
    *   `/data/snowflake`
    *   `/data/databricks`
    *   `/data/sql`

    You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.
