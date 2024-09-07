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
    
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    
    if post is None:
        return "Post not found", 404
    else:
        post_content = dict(post)
        return render_template('post.html', post=post_content)
    @app.route('/create_post', methods=['POST'])
    def create_post():
    '''
    Create a new post.
    Get the title and content from the request's form data.
    Insert the new post into the Database.
    Return a success message.
    '''
    title = request.form.get('title')
    content = request.form.get('content')
    
    if not title or not content:
        return "Both title and content are required", 400
    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return "Post created successfully", 201
    @app.route('/update_post', methods=['PUT'])
    def update_post():
    '''
    Update an existing post.
    Get the post's id, new title, and new content from the request's form data.
    Update the post in the Database.
    Return a success message.
    '''
    id = request.form.get('id')
    new_title = request.form.get('new_title')
    new_content = request.form.get('new_content')
    
    if not id or not new_title or not new_content:
        return "Id, new title and new content are required", 400
    else:
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (new_title, new_content, id))
        conn.commit()
        conn.close()
        return "Post updated successfully", 200
    @app.route('/delete_post', methods=['DELETE'])
    def delete_post():
    '''
    Delete an existing post.
    Get the post's id from the request's form data.
    Delete the post from the Database.
    Return a success message.
    '''
    id = request.form.get('id')
    
    if not id:
        return "Id is required", 400
    else:
        conn = get_db_connection()
        conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return "Post deleted successfully", 200
    
    if __name
