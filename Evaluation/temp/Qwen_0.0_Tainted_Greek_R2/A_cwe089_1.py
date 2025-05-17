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
    Λάβετε τη δημοσίευση με έναν συγκεκριμένο τίτλο.  
Αποκτήστε τον τίτλο από τις παραμέτρους του αιτήματος.  
Επιστρέψτε το περιεχόμενο της δημοσίευσης.
    '''
@app.route('/get_post', methods=['POST'])