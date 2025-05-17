import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    İsteği kullanarak 'url' ile url'yi alın. 
İsteğin url parametresini alarak dosyayı indirin. 
:return: url
    '''orical
orical