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
        if len(request.args) == 0:
            # If any param is provided in the URL, return an error.
            response = {
                'message': 'error',
                'reason': 'you-should-provide-one-param'
                }
            return render_template('login.html',response=response)

        # Else, return the title content.
        conn = get_db_connection()
        title = request.args['title']    
        query = 'SELECT * from post WHERE title = ?'
