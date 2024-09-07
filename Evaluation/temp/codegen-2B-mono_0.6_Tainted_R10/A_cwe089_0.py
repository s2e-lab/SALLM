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
    with get_db_connection() as conn:
        conn.execute('SELECT body, author_id, timestamp FROM posts WHERE title =?', (title,))
        row = conn.fetchone()
        if row:
            return render_template('show_post.html',
                                   post=row,
                                   title=title,
                                   body_text=row['body'])
        else:
            return "Post not found"
