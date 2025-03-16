import pymysql
from db import get_db_connection

def event_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE if not exists Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    event_date DATE NOT NULL,
    location VARCHAR(255),
    description TEXT,
    club_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id) ON DELETE CASCADE
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_event(name, description, date, location):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO events (name, description, date, location)
    VALUES (%s, %s, %s, %s)
    """
    
    cursor.execute(insert_query, (name, description, date, location))
    connection.commit()
    cursor.close()
    connection.close()

def get_all_events():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return events