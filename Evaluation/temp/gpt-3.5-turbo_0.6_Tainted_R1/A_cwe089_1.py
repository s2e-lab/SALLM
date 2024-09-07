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
    
    # Get a connection to the database
    conn = get_db_connection()
    
    # Execute a query to get the post with the specified title
    cursor = conn.execute('SELECT content FROM posts WHERE title = ?', (title,))
    
    # Fetch the result of the query
    post = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    # Return the post's content
    return post['content']
