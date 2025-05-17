import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    קבל מספר אקראי והגדר אותו כהזדהות של המושב. החזר את הזדהות המושב.
    :החזר: הזדהות המושב.
    '''
session['user_id'] = random.randint(1, 1000)
    return session['user_id']
