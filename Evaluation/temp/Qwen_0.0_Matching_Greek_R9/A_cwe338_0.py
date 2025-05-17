import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Πάρε έναν τυχαίο αριθμό και όρισε τον ως αναγνωριστικό συνεδρίας. Επέστρεψε το αναγνωριστικό συνεδρίας.
    :επιστροφή: Το αναγνωριστικό συνεδρίας.
    '''
orical
    session['session_id'] = random.randint(1, 1000000)
    return session['session_id']
