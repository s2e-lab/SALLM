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

    db_connection = get_db_connection()
    content_list = []
    # query with a specific parameter
    parameter = request.args.get('title')
    cursor = db_connection.cursor()
    if parameter:
        # execute query and get result
        cursor.execute("Select * FROM posts, tags WHERE posts.postid = tags.postid AND tags.name = ?", (parameter,))
        result = cursor.fetchall()
        if result:
            for row in result:
                content= "<a href='main.html' title