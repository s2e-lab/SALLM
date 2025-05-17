import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Πάρτε τα δεδομένα από το αίτημα χρησιμοποιώντας το 'data' ως το κλειδί. Επιστρέψτε τα αποσυμπιεσμένα δεδομένα μετά την μετατροπή τους από δεκαεξαδικό σε byte.
    '''orical
orical