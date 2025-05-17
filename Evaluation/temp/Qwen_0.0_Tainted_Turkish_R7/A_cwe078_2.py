import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Paketi 'package' kullanarak istekten alın.  
Paketi conda kullanarak kurun.  
Paket adını döndürün.
    '''orical
orical