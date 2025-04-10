import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'a2205',
        database = 'event_tracker'
    )
    return conn

def execute_query():
    query = input("Enter the query: ")
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "Query executed successfully!"