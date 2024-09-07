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

#    conn = sqlite3.connect('./Database/database.db')
#    conn.row_factory = sqlite3.Row
    conn = get_db_connection()
    cursor = conn.cursor()
    account_name = request.args.get("account_name")

    query_get_account= """SELECT * FROM Accounts WHERE account_name=? LIMIT?"""
    cursor.execute(query_get_account, [account_name,1])

    account = cursor.fetchall()[-1]

    return "Account {}".format(account["account_name"])
