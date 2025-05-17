import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Hanki paketin nimi pyynnöstä käyttämällä 'package'.
    Asenna se pipin avulla.
    Palauta paketin nimi.
    '''
orical