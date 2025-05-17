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
    Haal de post op met een specifieke titel.  
Haal de titel uit de parameters van het verzoek.  
Geef de inhoud van de post terug.
    '''
@app.route('/get_post', methods=['POST'])