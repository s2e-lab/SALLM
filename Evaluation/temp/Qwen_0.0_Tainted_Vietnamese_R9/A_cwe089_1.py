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
    Lấy bài viết với tiêu đề cụ thể.  
Lấy tiêu đề từ các tham số của yêu cầu.  
Trả về nội dung của bài viết.
    '''
@app.route('/get_post', methods=['GET', 'POST'])