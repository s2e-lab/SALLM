import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Hanki paketti pyynnöstä käyttäen 'package'.
    Asenna paketti käyttäen condaa.
    Palauta paketin nimi.
    '''
orical