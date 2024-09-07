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

    session_id = random.randint(1, 10000)
    session['id'] = session_id
    return "Your session ID is %s" % session['id'] 
    
    