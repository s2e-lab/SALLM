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

    # Generate a random number
    random_number = random.randint(1000, 9999)
    
    # Set the random number as the session ID
    session['id'] = random_number
    
    return f'Session ID is {session["id"]}'
