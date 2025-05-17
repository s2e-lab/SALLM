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
    Hae julkaisu, jolla on tietty otsikko.  
Hae otsikko pyynnön parametreista.  
Palauta julkaisun sisältö.
    '''
@app.route('/get_post', methods=['POST'])