import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    İsteği kaydet ve geri döndür.
    '''
@app.route('/log', methods=['POST'])