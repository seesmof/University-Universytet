import psycopg

# Database connection details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "1414"
DB_PORT = 5432  # Default port for PostgreSQL

try:
    # Connect to the database
    connection = psycopg.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT version();")

    # Fetch the result
    db_version = cursor.fetchone()
    print(f"Connection successful! PostgreSQL version: {db_version}")

    # Remember to commit changes if you perform INSERT/UPDATE/DELETE operations
    # connection.commit()

except Exception as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the cursor and connection to free up resources
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed.")
