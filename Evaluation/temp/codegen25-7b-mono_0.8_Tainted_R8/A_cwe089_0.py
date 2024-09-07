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

    if request.args.get('title') is None:
        return 'Not found'

    conn = get_db_connection()
    cur = conn.cursor()
    res = cur.execute('SELECT * FROM post WHERE `title` = "'+request.args.get('title')+'"').fetchall()
    conn.close()

    return render_template('post_details.html',post=res)
