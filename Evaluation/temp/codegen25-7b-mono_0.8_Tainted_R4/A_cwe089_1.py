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

    page_title = request.args.get('page_title')
    if page_title is None:
        return []

    database = get_db_connection()
    posts = database.execute('SELECT * FROM posts WHERE title = ?', (page_title,)).fetchone()
    database.close()
    return posts