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

    default_content = '\n{% with page=page %}\n     {{ page.content }}'
    conn = get_db_connection()
    title = request.args.get('title') # the query parameters are available in the request.args dictionary
    if title is None:
        title = 'Test'
    contents = conn.execute('SELECT content FROM pages WHERE title = ?', (title,)).fetchone()#returns a list
    return contents[0].replace('{%block title%}','').replace('{%endblock%}', '').