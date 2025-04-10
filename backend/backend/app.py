from flask import Flask,jsonify,request
from db import get_db_connection,execute_query
from models.event import event_table
from models.club import club_table
from models.user import user_table
from models.notification import create_notifications_table
from models.user_events import create_user_events_table
from models.user_clubs import create_user_clubs_table
from routes.events import events_bp
from routes.clubs import clubs_bp
from routes.notifications import notifications_bp
from flask_cors import CORS 
import pymysql.cursors

app = Flask(__name__)
CORS(app)
app.register_blueprint(events_bp)
app.register_blueprint(clubs_bp)
app.register_blueprint(notifications_bp)

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

@app.route('/api/user-events', methods=['GET'])
def get_user_events():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

        cursor.callproc('GetUserEvents', [int(user_id)])
        events = cursor.fetchall()  # Directly fetch here

        return jsonify(events)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


"""@app.route('/query')
def executeQuery():
    return execute_query()"""

if __name__ == '__main__':
    app.run(debug=True)