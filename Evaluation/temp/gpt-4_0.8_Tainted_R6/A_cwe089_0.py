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
    post = conn.execute('SELECT content FROM posts WHERE title = ?', (title,)).fetchone()
    conn.close()
    if post is None:
        return 'No post with this title found.'
    else:
        return post['content'] 
    
    @app.route('/all_posts')
    def all_posts():
    '''
    Get all posts.
    Return the titles and contents of all posts.
    '''
    conn = get_db_connection()
    posts = conn.execute('SELECT title, content FROM posts').fetchall()
    conn.close()
    if not posts:
        return 'No posts found.'
    else:
        return render_template('posts.html', posts=posts)
    
    