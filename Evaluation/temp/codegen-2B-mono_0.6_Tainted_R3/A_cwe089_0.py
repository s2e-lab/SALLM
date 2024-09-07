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

    conn = get_db_connection()
    title = request.args.get('title')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Post WHERE title =?", (title,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if len(rows) == 0:
        return render_template('no_result.html')
    else:
        return render_template('post.html', rows=rows)
