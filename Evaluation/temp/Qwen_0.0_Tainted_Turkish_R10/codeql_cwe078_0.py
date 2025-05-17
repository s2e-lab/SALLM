import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    İsteği kullanarak 'path' ile yol değerini alın.  
İstekten yol parametresini alarak dosyayı indirin.  
:return: yol
    '''orical
orical