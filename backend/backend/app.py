from flask import Flask,jsonify,request
from db import get_db_connection,execute_query
from models.event import event_table, insert_event, get_all_events
from models.club import club_table, insert_club, get_all_clubs
from models.user import user_table, insert_user, get_all_users
from models.notification import create_notifications_table, insert_notification, get_notifications_for_user
from models.user_events import create_user_events_table, register_user_for_event, get_user_events
from models.user_clubs import create_user_clubs_table, add_user_to_club, get_user_clubs
from routes.events import events_bp
from flask_cors import CORS 
import pymysql

app = Flask(__name__)
CORS(app)
app.register_blueprint(events_bp)

@app.route('/')
def home():
    return 'API is running!'

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

"""@app.route('/api/user-events', methods=['GET'])
def get_user_events():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        cursor = db.cursor(dictionary=True)
        cursor.callproc('GetUserEvents', [int(user_id)])

        for result in cursor.stored_results():
            events = result.fetchall()
        
        return jsonify(events)
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to fetch user events"}), 500

@app.route('/query')
def executeQuery():
    return execute_query()"""

if __name__ == '__main__':
    app.run(debug=True)