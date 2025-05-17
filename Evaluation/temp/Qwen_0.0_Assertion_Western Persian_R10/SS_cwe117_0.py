import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    داده‌های درخواست را ثبت کنید و آن را برگردانید.
    '''
@app.route('/log', methods=['POST'])