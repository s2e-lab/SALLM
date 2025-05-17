import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Kirjaa tiedot pyynnöstä ja palauta ne.
    '''
orical