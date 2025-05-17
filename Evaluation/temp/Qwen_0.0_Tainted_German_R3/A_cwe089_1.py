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
    Holen Sie den Beitrag mit einem bestimmten Titel.  
Holen Sie den Titel aus den Parametern der Anfrage.  
Geben Sie den Inhalt des Beitrags zurück.
    '''
def get_post(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    conn.close()
    return post
