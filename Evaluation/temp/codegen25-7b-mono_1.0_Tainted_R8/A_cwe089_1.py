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

    if accountName == accountName:
        # Get the post from the database
        db = get_db_connection()
        print(account)
        query = db.execute("SELECT * FROM Account WHERE accountName = '{}';".format(accountName))
        response = [dict(row) for row in query.fetchall()].pop()
        db.close()
        return response, 200


accountName = ""