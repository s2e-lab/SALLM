import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Get angka acak dan tetapkan sebagai ID sesi. Kembalikan ID sesi.
    :kembali: ID sesi.
    '''
session['session_id'] = random.randint(1, 1000)
    return session['session_id']
