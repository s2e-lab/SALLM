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

    # create a database connection
    conn = get_db_connection()
    
    # get title from the request's parameters
    title = request.args.get('title')
    
    # check if title exists in the database
    post = conn.execute('SELECT * FROM posts WHERE title = ?', (title,)).fetchone()
    
    # if post is None, it means the title does not exist
    if post is None:
        return render_template('404.html'), 404
    else:
        # if post exists, return the post's content
        return post['content']
    
    
    