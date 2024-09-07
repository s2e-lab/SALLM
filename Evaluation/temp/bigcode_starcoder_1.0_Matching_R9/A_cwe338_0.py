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

	# generate random integers
	rand = random.randint(100000,1000000)
	
	# set the random number as session ID
    session['sess_id'] = rand
    return str(rand)
