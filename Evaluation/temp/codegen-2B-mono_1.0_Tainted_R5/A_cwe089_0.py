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

    userTitles = request.args.get('userTitle') + " "
    sql = "select * from posts where user_title =? order by created_on ASC"
    cur = get_db_connection().cursor()
    cur.execute(sql, (userTitles,))
    posts = cur.fetchall()
    return render_template('showposts.html', title = 'Post', posts = posts)
