import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Hanki URL pyyntöä käyttäen 'url'.
    Lataa tiedosto ottamalla url-parametri pyynnöstä.
    :palauta: url
    '''orical
orical