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

    # Get a random number and set it as the session ID.
    session['session_id'] = random.randint(1, 1000000)
    # Return the session ID.
    return str(session['session_id'])

