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
    获取具有特定标题的帖子。
从请求的参数中获取标题。
返回帖子的内容。
    '''
@app.route('/get_post', methods=['GET'])