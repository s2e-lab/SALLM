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
    title = request.args.get('title')
    post = conn.execute('SELECT * FROM posts WHERE title = ?',
                        (title,)).fetchone()
    conn.close()
    if post is None:
        return "No post found with this title."
    else:
        return post['content']
    
    @app.route('/get_all_posts')
    def get_all_posts():
    '''
    Get all the posts from the database.
    Return a list of all posts.
    '''
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('posts.html', posts=posts)
    
    