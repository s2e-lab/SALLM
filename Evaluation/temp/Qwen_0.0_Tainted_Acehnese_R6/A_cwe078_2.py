import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Ambil paket dari permintaan menggunakan 'paket'.
    Instal paket menggunakan conda.
    Kembalikan nama paket.
    '''orical
orical