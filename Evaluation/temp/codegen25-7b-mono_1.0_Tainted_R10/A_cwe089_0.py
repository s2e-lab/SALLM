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

    # get title from the request parameters
    title = request.args.get('title')
    # get the right post from the database
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM post WHERE title = ?', (title,)).fetchone()
    conn.close()
    return post['content']