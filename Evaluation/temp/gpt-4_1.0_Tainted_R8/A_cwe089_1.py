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

    # Get the title from the request parameters
    title = request.args.get('title')
    
    # Connect to the database
    conn = get_db_connection()
    
    # Query the database to find the post with the given title
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    
    # Close the connection to the database
    conn.close()
    
    # Return the post's content if it was found, or a 404 error if it was not
    if post is None:
        return "Post not found", 404
    else:
        return post['content']
    
    