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
    with conn:
        cur = conn.cursor()
        post = cur.execute('SELECT * FROM posts WHERE title =?', (title,)).fetchone()
        cur.close()
    if post is None:
        return render_template('error.html', message = 'The post you are looking for does not exist!')
    else:
        return render_template(
            'post.html',
            post = post
        )
