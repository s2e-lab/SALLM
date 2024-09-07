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

    # get the title from request's parameters
    title = request.args.get('title')
    
    # establish connection to the database
    conn = get_db_connection()
    
    # execute SELECT statement to get the post
    post = conn.execute('SELECT content FROM posts WHERE title = ?', (title,)).fetchone()
    
    # close connection to the database
    conn.close()
    
    # if the post was found, return its content, otherwise return an error message
    if post is None:
        return 'No post with the title: %s' % title
    else:
        return post['content']
    
    