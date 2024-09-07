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

    sessionid = random.randint(10000, 10000000)
    session['sessionid'] = sessionid
    print("setting session['sessionid'] to {}".format(sessionid))
    return "Your session ID is {}!".format(str(sessionid))
