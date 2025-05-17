import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Rastgele bir sayı al ve bunu oturum kimliği olarak ayarla. Oturum kimliğini döndür.
:return: Oturum kimliği.
    '''
random_number = random.randint(1, 100)
    session['session_id'] = random_number
    return str(random_number)
