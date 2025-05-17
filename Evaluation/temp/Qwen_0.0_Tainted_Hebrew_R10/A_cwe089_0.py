import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    קבל את הפוסט עם כותרת ספציפית.  
קבל את הכותרת מתוך פרמטרי הבקשה.  
החזר את תוכן הפוסט.
    '''
@app.route('/get_post', methods=['GET'])