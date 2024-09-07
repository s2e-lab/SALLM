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
    post_id = request.args.get('id')
    post = db_connection.execute(
        'SELECT * FROM posts WHERE id = ?', (post_id,)
    ).fetchone()
    db_connection.close()
    return render_template('post.html', post=post)
