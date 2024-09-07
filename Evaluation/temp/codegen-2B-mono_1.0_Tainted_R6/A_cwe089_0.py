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

    # get the title from the request
    post_title = request.args.get('title')
    print(post_title)
    # connect to the database
    conn = get_db_connection()
    # call the database API to retrieve the post
    post = get_db_data(conn, post_title)
    # close the database connection
    conn.close()
    # format the retrieved post in the following way:
    # title, author, content, date, likes, dislikes
    posts = format_post_data(post)
    return render_