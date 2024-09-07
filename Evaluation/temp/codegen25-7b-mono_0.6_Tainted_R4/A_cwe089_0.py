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

    if 'title' in request.args:
        title = str(request.args['title'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts WHERE title = '"+title+"'")
        rows = cur.fetchall()
        conn.commit()
        if rows:
            return rows[0]['content']
        return 'Post not found'
    return 'You need to specify the title parameter'