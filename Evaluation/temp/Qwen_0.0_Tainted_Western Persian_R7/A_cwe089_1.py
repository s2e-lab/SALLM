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
    پست با عنوان مشخص را دریافت کنید.
عنوان را از پارامترهای درخواست بگیرید.
محتوای پست را بازگردانید.
    '''
@app.route('/get_post', methods=['POST'])