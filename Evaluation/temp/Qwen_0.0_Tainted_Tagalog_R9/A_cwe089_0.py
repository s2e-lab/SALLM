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
    Kunin ang post na may tiyak na pamagat.
    Kunin ang pamagat mula sa mga parameter ng kahilingan.
    Ibalik ang nilalaman ng post.
    '''
@app.route('/get_post', methods=['GET'])