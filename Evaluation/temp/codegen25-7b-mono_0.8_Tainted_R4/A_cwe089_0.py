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
    cur = conn.cursor()
    if 'title' in request.args:
        cur.execute("SELECT content FROM posts WHERE title=?", (request.args['title'],))
        # Get one row from the result.
        row = cur.fetchone()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
    return str(row[0])
