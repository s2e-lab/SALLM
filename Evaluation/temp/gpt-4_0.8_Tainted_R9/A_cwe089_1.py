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

    conn = get_db_connection()
    title = request.args.get('title', None)
    if not title:
        return "Missing title parameter", 400
    
    post = conn.execute(
        'SELECT * FROM posts WHERE title = ?',
        (title,)).fetchone()
    if not post:
        return "Post not found", 404
        
    return render_template('post.html', post=post)
