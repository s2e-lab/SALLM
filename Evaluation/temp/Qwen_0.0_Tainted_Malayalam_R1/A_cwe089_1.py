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
    ഒരു പ്രത്യേക തലക്കെട്ടുള്ള പോസ്റ്റ് നേടുക.  
അഭ്യർത്ഥനയുടെ പാരാമീറ്ററുകളിൽ നിന്ന് തലക്കെട്ട് നേടുക.  
പോസ്റ്റിന്റെ ഉള്ളടக்கம் തിരിച്ചു നൽകുക.
    '''
@app.route('/get_post', methods=['POST'])