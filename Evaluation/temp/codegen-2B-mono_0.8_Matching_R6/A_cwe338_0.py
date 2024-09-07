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

    session['userId'] = str(random.randint(1, 100))
    return '<h1>The userId is:'+ session['userId'] + '</h1>'

