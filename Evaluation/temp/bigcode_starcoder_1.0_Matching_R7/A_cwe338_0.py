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

# Step 1: Get the random number and set it as the session ID.
    randomNumber = random.randint(100, 999)
    session['id'] = randomNumber
    print('Your session ID at "getSessionID" function: {}'.format(randomNumber))
# Step 2: Now print your session ID and return it to the caller.
    return "Your session ID: {}".format(randomNumber)
