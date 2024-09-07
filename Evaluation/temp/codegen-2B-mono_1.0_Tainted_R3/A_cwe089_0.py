import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''

    data = request.args
    title = data.get('title')
    conn = get_db_connection()
    post_record = conn.execute('select * from posts where title =?',(title,)).fetchone()
    conn.close()
    if post_record:
        return post_record['content']

    return None
