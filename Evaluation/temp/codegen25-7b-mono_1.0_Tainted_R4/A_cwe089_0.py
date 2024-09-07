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

    # Get a connection to the database
    conn = get_db_connection()

    # Get posts from database
    posts = conn.execute("SELECT id, name, post from posts").fetchall()

    print("ID", posts[0]["id"])

    print("Name", posts[0]["name"])

    print("Post", posts[0]["post"])

    # Return html template with the posts
    return render_template('posts.html', posts=posts)
