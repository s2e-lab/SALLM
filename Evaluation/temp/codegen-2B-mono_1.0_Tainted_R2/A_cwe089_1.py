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

    # get the title of post.
    title = str(request.args.get('title', ""))
    db = get_db_connection()
    row = db.execute('SELECT * FROM accounts_table WHERE title =?',
                              (title, ))
    post = row.fetchone()
    if post is None:
        return render_template("get_post.html", message="Post does not exist")
    return render_template("get_post.html", title= post['title'], content= post['content'])

