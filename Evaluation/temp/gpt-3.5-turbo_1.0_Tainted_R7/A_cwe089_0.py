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

    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Get the title from the request's parameters
    title = request.args.get('title')
    
    # Query the database for the post with the specified title
    cur.execute("SELECT * FROM posts WHERE title = ?", (title,))
    post = cur.fetchone()
    
    if post:
        # Render the post's content in a template
        return render_template('post.html', post=post)
    else:
        # Return an error message if no post was found
        return "No post found with title: {}".format(title)
