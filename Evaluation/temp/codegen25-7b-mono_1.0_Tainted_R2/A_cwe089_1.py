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

    title = request.args.get('post_title')
    print("get_account")
    # Open database in read mode only
    connection = get_db_connection()
    print("get_account")
    try:
        # Get all the posts from the database as a list
        posts = connection.execute("SELECT id,username,email,password,address,dob,phonenum,role,gender,profilepic,post_text FROM Userinfo WHERE username=?",[title]).fetchall()
        # Initialise index to 1 to avoid index errors when listing posts
