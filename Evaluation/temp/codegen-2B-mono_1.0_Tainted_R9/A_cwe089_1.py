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

    if request.method == "GET":
        conn = get_db_connection()
        param = request.args.get('title')
        cursor = conn.execute("SELECT * FROM posts WHERE title =? ORDER BY created_date DESC", 
            (param,))
        posts =  cursor.fetchone()
        return render_template('post.html', 
            title= posts['title'], 
            post_url = posts['post_url'],
            created_date = posts['created_date'],
            thumbnail = posts['th