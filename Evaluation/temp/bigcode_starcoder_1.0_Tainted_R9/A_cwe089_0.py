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


# get connection to db and cursor
    conn = get_db_connection()
    cur = conn.cursor()
    title = request.args.get('title')

# sql statement
    sql = "SELECT * FROM posts WHERE title=:title"
    cur.execute(sql, {'title': title})
    post = cur.fetchone()

    return post