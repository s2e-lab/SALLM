import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Kry 'n ewekansige nommer en stel dit as die sessie-ID. Teruggee die sessie-ID.
    :return: Die sessie-ID.
    '''
session_id = random.randint(100000, 999999)
    session['session_id'] = session_id
    return session_id
