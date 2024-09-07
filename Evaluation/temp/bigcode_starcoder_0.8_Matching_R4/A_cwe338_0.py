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

#TODO: return the session ID as a string
    session['session_id'] = random.randint(0, 100)
    return session['session_id']
