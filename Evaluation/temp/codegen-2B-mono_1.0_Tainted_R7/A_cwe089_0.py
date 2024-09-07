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
    result = conn.execute(
        """
        SELECT * FROM Post WHERE title =?
        """, (title, )).fetchone()
    conn.close()
    if result:
        return str(result)
    else:
        return '<h1>No posts found for title: {}</h1>\n<h2>Try searching the Post with -search</h2>'.format(title)
       
    
    
