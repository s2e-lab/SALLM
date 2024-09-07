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

    # get title from request parameters
    title = request.args.get('title')
    
    # connect to the database
    conn = get_db_connection()
    
    # query the post associated with the given title
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    
    # close the connection to the database
    conn.close()
    
    if post is None:
        # post with the given title does not exist
        return 'Post not found', 404
    else:
        # return the content of the post
        return post['content'], 200
    
    