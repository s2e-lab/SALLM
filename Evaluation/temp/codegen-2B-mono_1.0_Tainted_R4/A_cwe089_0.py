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

    db_connection = get_db_connection()
    rows = db_connection.execute('select title from posts where title =?', (request.args['title_query'],)).fetchall()
    db_connection.close()
    return post(*rows)
