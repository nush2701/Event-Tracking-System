from flask import Flask,jsonify
from db import get_db_connection,execute_query
from models.event import event_table, insert_event, get_all_events
from models.club import club_table, insert_club, get_all_clubs
from models.user import user_table, insert_user, get_all_users
from models.notification import create_notifications_table, insert_notification, get_notifications_for_user
from models.user_events import create_user_events_table, register_user_for_event, get_user_events
from models.user_clubs import create_user_clubs_table, add_user_to_club, get_user_clubs
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to event tracker"

@app.route('/create')
def test():
    try:
        club_table()
        user_table()
        event_table()
        create_notifications_table()
        create_user_clubs_table()
        create_user_events_table()
        return "tables created"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/query')
def executeQuery():
    return execute_query()

if __name__ == '__main__':
    app.run(debug=True)