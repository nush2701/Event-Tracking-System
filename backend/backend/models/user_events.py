from db import get_db_connection

def create_user_events_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS User_Events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        event_id INT NOT NULL,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status ENUM('Registered', 'Attended', 'Cancelled') DEFAULT 'Registered',
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE
    )
    """
    
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def register_user_for_event(user_id, event_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO User_Events (user_id, event_id) 
    VALUES (%s, %s)
    """
    
    cursor.execute(insert_query, (user_id, event_id))
    connection.commit()
    cursor.close()
    connection.close()

def get_user_events(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    select_query = "SELECT * FROM User_Events WHERE user_id = %s"
    cursor.execute(select_query, (user_id,))
    
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return events
