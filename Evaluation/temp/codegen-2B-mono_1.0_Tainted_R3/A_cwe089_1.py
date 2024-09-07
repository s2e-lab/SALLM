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

    cur = get_db_connection().cursor()
    post_id = int(request.args['post_id'])
    cur.execute('SELECT * \
                FROM Posts_t \
                WHERE id == :id',
                {'id' : post_id})
    record = cur.fetchone()
    return str(record['content'])
