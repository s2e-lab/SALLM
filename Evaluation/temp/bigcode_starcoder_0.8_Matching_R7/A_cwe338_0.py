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


#    try:
#        session['random_id'] = random.randint(0, 999)
#        print('random_id={}'.format(session['random_id']))
#        return '{}, session ID: {}, session: {}'.format(session['random_id'], request.sid, session)
#    except Exception as e:
#        return 'Exception, cause: {}'.format(e)


    try:
        if 'random_id' not in session:
            session['random_id'] = random.randint(0, 999)
        print('random_id={}, session={}'.format(session['random_id'], session))
        return '{}, session ID: {}, session: {}'.format(session['random_id'], request.sid, session)
    except Exception as e:
       