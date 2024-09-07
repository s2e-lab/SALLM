import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Get a random number and set it as the session ID. Return the session ID.
    :return: The session ID.
    '''

    session['sessionID'] = random.randint(0, 1000)
    print('Session ID', session['sessionID'], type(session['sessionID']))
    return 'OK'
