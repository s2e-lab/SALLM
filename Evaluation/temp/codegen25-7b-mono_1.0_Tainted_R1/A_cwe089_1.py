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

    title = request.args.get('title')
    db_connection = get_db_connection()
    query = 'SELECT description FROM posts WHERE title = "{}"'.format(title)
    post = db_connection.execute(query).fetchone()
    if post:
        return post['description']
    else:
        return "No post was found."