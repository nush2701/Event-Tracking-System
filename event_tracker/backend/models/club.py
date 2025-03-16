import pymysql
from db import get_db_connection

def club_table():
    conn = get_db_connection() 
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS clubs (
        club_id INT AUTO_INCREMENT PRIMARY KEY,
        club_name VARCHAR(255) NOT NULL UNIQUE,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_club(club_name, description):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO clubs (club_name, description)
    VALUES (%s, %s)
    """
    
    cursor.execute(insert_query, (club_name, description))
    connection.commit()
    cursor.close()
    connection.close()

def get_all_clubs():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM clubs")
    clubs = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return clubs