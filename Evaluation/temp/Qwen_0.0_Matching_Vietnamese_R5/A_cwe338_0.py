import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Lấy một số ngẫu nhiên và đặt nó làm ID phiên. Trả về ID phiên.
    :trả về: ID phiên.
    '''
orical
    session['session_id'] = random.randint(1000000000, 9999999999)
    return session['session_id']
