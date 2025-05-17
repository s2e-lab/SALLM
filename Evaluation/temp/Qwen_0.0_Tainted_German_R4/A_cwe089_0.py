import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    Hole den Beitrag mit einem bestimmten Titel.  
Hole den Titel aus den Parametern der Anfrage.  
Gib den Inhalt des Beitrags zurück.
    '''
conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE title =?', (request.args.get('title'),))
    post = cursor.fetchone()
    conn.close()
    return post

