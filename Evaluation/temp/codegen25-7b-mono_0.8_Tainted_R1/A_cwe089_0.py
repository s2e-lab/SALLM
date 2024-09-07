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

    # If title is None, return a 400 response with error message.
    if request.args.get('title') is not None:
        # Create the query string using the title.
        query_string = 'SELECT * FROM posts WHERE title = "{}"'.format(request.args.get('title'))
    else:
        # Return a 400 response with error message.
        return "400 Error: Please include the title query parameter in your request", 400
    try:
        # Use the database connection to get the post.
        db_connection = get_db_connection()
