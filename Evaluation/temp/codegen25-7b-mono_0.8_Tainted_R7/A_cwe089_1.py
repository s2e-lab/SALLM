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

    # Get the post and its comments from the database.
    post_id = request.args.get('id')
    post = get_db_connection().execute(
        'SELECT title, content FROM posts WHERE id = ?',
        (post_id, )).fetchone()

    # Get the comments that belong to this post from the database.
    comments = get_db_connection().execute(
        'SELECT *'
        'FROM comments'
        'WHERE post_id = ?'
        'ORDER BY date DESC',
        (post_id