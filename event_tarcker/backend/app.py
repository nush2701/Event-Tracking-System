from flask import Flask,jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':"welcome to event tracker"})

@app.route('/test_db')
def test():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select database();")
    db_name = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify({'message' : f'connected to database {db_name}'})

if __name__ == '__main__':
    app.run(debug=True)