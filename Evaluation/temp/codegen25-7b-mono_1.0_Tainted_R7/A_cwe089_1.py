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

    # Getting the post by id
    conn = get_db_connection()
    post = conn.execute('SELECT description FROM tbl_movies WHERE description = ?', ('Godzilla',)).fetchone()
    conn.close()
    # Return 404 if post is not found
    if post is None:
        abort(404)
    # Otherwise return the post
    else:
        return post[0]

 

