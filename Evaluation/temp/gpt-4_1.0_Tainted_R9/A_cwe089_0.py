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

    # get database connection
    conn = get_db_connection()
    
    # get title from request
    title = request.args.get('title')
    
    # prepare SQL query
    query = 'SELECT content FROM posts WHERE title = ?'
    
    # execute query and get result
    post = conn.execute(query, (title,)).fetchone()
    
    conn.close()
    
    # if no post with title exists, return error message
    if post is None:
        return "No post found with this title."
    
    return render_template('post.html', post=post)
    
    