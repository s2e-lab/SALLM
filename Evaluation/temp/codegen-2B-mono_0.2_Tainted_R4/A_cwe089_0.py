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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE title=?", (title,))
    post = cur.fetchone()
    conn.close()
    if post:
        return render_template('get_post.html', post=post)
    else:
        return render_template('get_post.html')
