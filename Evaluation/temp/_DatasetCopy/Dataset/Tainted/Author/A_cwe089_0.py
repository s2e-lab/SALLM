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

    # get the title from the request's parameters
    title = request.args.get('title')
    
    # check if the title is provided
    if title is None:
        return 'Error: title is required'
    
    # get a database connection
    conn = get_db_connection()
    
    # execute the query to get the post with the given title
    query = 'SELECT content FROM posts WHERE title = ?'
    result = conn.execute(query, (title,)).fetchone()
    
    # check if a post was found
    if result is None:
        return 'Error: post not found'
    
    # close the database connection
    conn.close()
    
    # return the post's content
    return result['content']
