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

#    # Check whether the table exists in the database
#    c = conn.cursor()
#    c.execute("SELECT count(name) FROM sqlite_master WHERE type='table'")
#    if c.fetchone()[0]==1:
    title = request.args.get("title")
    if title == "":
        return {"Error": "Post with title '"+title+"' not found."}
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = c.fetchone()
    if row:
        return {"title": row["title"], "content": row["content"]}
    else: