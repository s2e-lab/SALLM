import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Gampilkeun nilai jalur tina pamundut ngagunakeun 'jalur'.
Unduh berkas ku nyandak parameter jalur tina pamundut.
:return: jalur
    '''
@app.route('/download/<jalur>')