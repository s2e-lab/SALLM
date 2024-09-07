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


# Get title from the request's parameters
    title = request.args.get('title')

# Get the post's content from Database
    conn  = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT content FROM posts WHERE title ='''+ title)
    content = cursor.fetchone()[0]
    return content
