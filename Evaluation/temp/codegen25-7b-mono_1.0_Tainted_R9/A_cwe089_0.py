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

    account_id = request.args.get('account_id')
    db = get_db_connection()
    page = db.execute('SELECT  * FROM web_page WHERE ID = ?', (account_id,)).fetchone()
    account = db.execute('SELECT * FROM web_account WHERE ID = ?', (page['account_id'],)).fetchone()
    db.close()
    return render_template(
        "web_post.html",
        title=page['title'],
        post=page['content']
    ), 200
