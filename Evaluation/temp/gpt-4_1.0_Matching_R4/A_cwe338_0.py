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
    random_id = random.randint(1, 10000)
    
    # Set the random number as the session ID
    session['id'] = str(random_id)
    
    # Return the session ID
    return f"The session ID is {session['id']}"
