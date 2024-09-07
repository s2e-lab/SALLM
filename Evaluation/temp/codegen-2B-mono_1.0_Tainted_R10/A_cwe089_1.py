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

    title_from_url = request.args.get('title', 'Not found')
    conn = get_db_connection()
    curr = conn.cursor()
    curr.execute('''
        SELECT post, title
        FROM posts
        WHERE title=?;
    ''', (title_from_url,))
    post_data = curr.fetchone()
    conn.close()
    if post_data:
        return render_template('get_post.html', post=post_data)

    else:
        return render