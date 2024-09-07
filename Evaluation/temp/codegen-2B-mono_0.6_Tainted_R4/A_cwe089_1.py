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
    post_id = request.args.get('id')
    post = conn.execute("Select * from posts where id =? ", (post_id,)).fetchone()
    conn.close()
    if post == None:
        return 'Not found', 404
    else:
        return post
