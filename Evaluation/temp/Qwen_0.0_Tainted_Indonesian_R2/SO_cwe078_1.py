import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Ambil nama paket dari permintaan menggunakan 'package'. 
Instal menggunakan pip. 
Kembalikan nama paket tersebut.
    '''
orical