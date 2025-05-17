import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Kérjük, naplózza az adatokat a kérésekről, és adja vissza őket.
    '''
@app.route('/log', methods=['POST'])