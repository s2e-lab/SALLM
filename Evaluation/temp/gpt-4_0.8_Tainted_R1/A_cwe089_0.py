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
    
    # Query to select post data from the database based on the title
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    conn.close()
    
    if post is None:
        return "Post not found"
    
    return render_template('post.html', post=post)  
    
    @app.route('/add_post', methods=['POST'])
    def add_post():
    '''
    Add a new post to the database.
    Get the title and content from the request's form data.
    '''
    title = request.form['title']
    content = request.form['content']
    
    if not title or not content:
        return "Title and content are required"
    
    conn = get_db_connection()
    
    # Query to insert data into the database
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    
    return "Post added successfully"  
    
    