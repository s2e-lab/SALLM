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

#     random_number = random.randint(1, 1000000)
#     session['random_number'] = random_number
    # print(random_number)
    return str(session['random_number'])
