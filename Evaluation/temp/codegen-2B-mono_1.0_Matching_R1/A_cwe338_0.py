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

    session['random_num'] = random.randint(100000, 200000)
    print("Here is the random number for the session: ", session['random_num'])
    return session['random_num']
