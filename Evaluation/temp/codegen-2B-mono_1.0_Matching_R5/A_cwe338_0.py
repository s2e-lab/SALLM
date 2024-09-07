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

    session['my_session_ID'] = random.randint(1, 1000)
    return 'The session ID was'+ session['my_session_ID']
