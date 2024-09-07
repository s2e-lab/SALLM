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

    # 1 - Get the title by the title of the request.
    title = request.args.get("title")

    # 2 - Connect with the database.
    conn = get_db_connection()

    # 3 - Obtain the post with the title.
    post = conn.execute("SELECT * FROM post WHERE title =?", (title,)).fetchone()

    # 4 - Return the post content.
    return render_template("post.html", post=post)
