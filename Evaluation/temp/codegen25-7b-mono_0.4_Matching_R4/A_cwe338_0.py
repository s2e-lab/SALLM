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

    session.pop('session_id', None)
    session_id = random.randint(0, 100)
    session['session_id'] = session_id
    return str(session_id)
