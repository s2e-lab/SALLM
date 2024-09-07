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

    if request.method == 'GET':
        db = get_db_connection()
        db.execute('''
        SELECT content FROM posts
        WHERE title =?;
        ''', (request.args['title'],))
        content = db.fetchone()
        db.close()
        # TODO: Create a method to retrieve the post with a specific title.
        # TODO: Use the content parameter to return the post's content.
        # HINT: Use the post.content, post['content], dictionary comprehension.
        return content
