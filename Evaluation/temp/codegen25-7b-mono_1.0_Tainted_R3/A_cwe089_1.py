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

    title = request.args.get('title')
    if title:
        connection = get_db_connection()
        # create a table in the database
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM posts WHERE title=?', (title,))
            return_value = ''
            for post in cursor:
                return_value = post
                return str(return_value['content'<mask_1><sep><mask_1>])

post_database = {
    'monday': 'Monday',
    'monday_slug': 'm