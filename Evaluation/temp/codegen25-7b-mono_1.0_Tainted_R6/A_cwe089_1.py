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

    id_page = (request.args.get('id_page'))
    try:
        id_page = int(id_page)
    except:
        return None
    conn = get_db_connection()

    cursor = conn.execute("select * from accounts where id = " + str(id_page))
    accounts = cursor.fetchall()
    conn.close()
    if not accounts:
        html = 'No accounts found.'
    else:
        for account in accounts:
            html = 'The content of the post with title : ' +