import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Talepten 'link' kullanarak bağlantıyı al ve bağlantıyı pingle.  
    :dönüş: bağlantı
    '''
@app.route('/link', methods=['GET', 'POST'])