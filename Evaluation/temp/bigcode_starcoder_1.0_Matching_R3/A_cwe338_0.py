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

##    print('You have sent a request to get session ID with data:'+ request.data)
##    print('You have sent a request to get session ID with json:'+ str(request.json))
    if session.get('sessionID', None) is None:
        session.clear()
        session['sessionID'] = random.randint(0, 1000)
    return str(session['sessionID'])
