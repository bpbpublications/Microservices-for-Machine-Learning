
import mysql.connector

class RecommendationDao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.conn.cursor()

    def add_log(self, user_id, recommendation):
        sql = "INSERT INTO recommendation_log (user_id, recommendation) VALUES (%s, %s)"
        val = (user_id, recommendation)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def get_user_preferences(self, user_id):
        sql = "SELECT preferences FROM user_preferences WHERE user_id=%s"
        val = (user_id, )
        self.cursor.execute(sql, val)
        return self.cursor.fetchone()
