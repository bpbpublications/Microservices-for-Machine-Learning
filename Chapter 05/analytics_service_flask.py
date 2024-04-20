
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

class AnalyticsDao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.conn.cursor()

    def add_data(self, new_data):
        sql = "INSERT INTO analytics_data (data_field) VALUES (%s)"
        val = (new_data, )
        self.cursor.execute(sql, val)
        self.conn.commit()

    def get_data(self):
        sql = "SELECT * FROM analytics_data"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

analyticsDao = AnalyticsDao()

@app.route('/analytics', methods=['POST'])
def collect_data():
    data = request.json
    analyticsDao.add_data(data)
    return jsonify({'status': 'data collected'})

@app.route('/analytics', methods=['GET'])
def get_analytics():
    return jsonify({'data': analyticsDao.get_data()})
