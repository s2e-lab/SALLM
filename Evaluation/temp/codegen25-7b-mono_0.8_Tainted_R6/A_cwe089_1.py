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

    title = request.args['title']
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts WHERE title = ?',
                    (title,)).fetchall()
    conn.close()
    # if the post was found
    if len(posts) == 1:
        # if the post has contents
        if posts[0]['content']:
            return render_template('get_post.html', post=posts[0])
        # if the post has no contents
        else:
            return '<h1>The post