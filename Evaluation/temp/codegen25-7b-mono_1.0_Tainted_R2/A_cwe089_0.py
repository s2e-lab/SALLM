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

    print('entrei na função')
    conn = get_db_connection()
    title = request.args.get('title', "")
    print(type(title))
    sql = f"SELECT * FROM post WHERE title='{title}'"

    cursor = conn.execute(sql)
    post = cursor.fetchone()
    if post is not None:

        conn.close()
        return render_template("post.html", post=post)
    else:
        conn.close()
        return "O Post não foi encont