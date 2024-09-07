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

    if request.method == 'GET':
        db_connection = get_db_connection()
        title = request.args.get('title', None) #request.args.get('title', False) 없으면 None
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM POST WHERE title =?", (title,))

    '''
    Get the posts of a specific user.
    Get the username from the request's parameters.
    Return the posts of that user.
    '''
    elif request.method