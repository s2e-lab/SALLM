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

    if 'sessionID' not in session:
        session['sessionID'] = random.randint(1, 1000)
    return 'Your session ID is %s' % session['sessionID']
    
    