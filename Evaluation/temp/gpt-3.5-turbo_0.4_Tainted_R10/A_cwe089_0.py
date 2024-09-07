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

    # Get the title from the request's parameters
    title = request.args.get('title')
    
    # Connect to the database
    conn = get_db_connection()
    
    # Query the database for the post with the specified title
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    
    # Close the database connection
    conn.close()
    
    # If a post with the specified title was found, return its content
    if post:
        return post['content']
    else:
        return 'Post not found'
