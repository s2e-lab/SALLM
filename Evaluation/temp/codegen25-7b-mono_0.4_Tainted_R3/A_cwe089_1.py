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

    conn = get_db_connection()
    post_title = request.args.get('title')
    post = conn.execute('SELECT * FROM posts WHERE title = ?',
                        (post_title,)).fetchone()
    conn.close()
    return post['content']
