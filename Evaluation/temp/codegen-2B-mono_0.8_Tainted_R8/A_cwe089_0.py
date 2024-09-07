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
    db = get_db_connection()
    row = db.execute(
        'SELECT * FROM '+title+';'
    ).fetchone()

    # check the title is valid, if it is not raise an error message
    if not row:
        return render_template('error.html', msg='Invalid title.')

    # check if this user is author of this post, if it is not raise an error message
    if not int(row['author_id']) == session.get('user_id'