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
    conn = get_db_connection()
    db_cursor = conn.cursor()
    db_cursor.execute("SELECT * FROM posts WHERE title = ?", (title, ))
    account = db_cursor.fetchone()
    conn.close()
    if account == None:
        return render_template("error.html", message="No post was found with that title!")
    else:
        post = {
        "id": account["id"],
        "title": account["title"],
