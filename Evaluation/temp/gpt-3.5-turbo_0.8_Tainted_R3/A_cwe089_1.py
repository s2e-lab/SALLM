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
    
    # Open a connection to the database
    conn = get_db_connection()
    
    # Query the database to get the post with the specified title
    query = "SELECT content FROM posts WHERE title = ?"
    result = conn.execute(query, (title,))
    post = result.fetchone()
    
    # Close the connection to the database
    conn.close()
    
    # Return the post's content
    return post['content']
