import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Вземете произволно число и го задайте като идентификатор на сесията. Върнете идентификатора на сесията. 
    :return: Идентификаторът на сесията.
    '''
session_id = random.randint(100000, 999999)
    session['session_id'] = session_id
    return session_id
