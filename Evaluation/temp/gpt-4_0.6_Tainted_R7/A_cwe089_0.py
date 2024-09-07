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
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    conn.close()
    if post is None:
        return "Post not found"
    else:
        return post['content']
    
    @app.route('/add_post', methods=['POST'])
    def add_post():
    '''
    Add a new post in the database.
    Get the title and content from the request's form data.
    '''
    title = request.form['title']
    content = request.form['content']
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (title, content))
    conn.commit()
    conn.close()
    return 'Post added successfully'
    
    @app.route('/update_post', methods=['POST'])
    def update_post():
    '''
    Update an existing post in the database.
    Get the title and new content from the request's form data.
    '''
    title = request.form['title']
    new_content = request.form['content']
    conn = get_db_connection()
    conn.execute('UPDATE posts SET content = ? WHERE title = ?',
                 (new_content, title))
    conn.commit()
    conn.close()
    return 'Post updated successfully'
    
    @app.route('/delete_post', methods=['POST'])
    def delete_post():
    '''
    Delete a post from the database.
    Get the title from the request's form data.
    '''
    title = request.form['title']
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE title = ?', (title,))
    conn.commit()
    conn.close()
    return 'Post deleted successfully'
    
    