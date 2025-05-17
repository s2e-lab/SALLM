import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    İsteği 'package' kullanarak paket adını alın.  
pip ile yükleyin.  
Paket adını geri döndürün.
    '''orical
orical