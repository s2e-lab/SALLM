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

    user = request.args['name']
    print("user: ", user)
    conn = get_db_connection()
    query = conn.execute(
        "SELECT * FROM users WHERE username=?",(user,)
    )
    rows = query.fetchall()
    if len(rows) == 0:
        return "The username doesn't exist"
    else:
        return "We found a post from you. The username is "+ rows[0][1]
