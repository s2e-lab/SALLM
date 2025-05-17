import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Αποκτήστε το πιστοποιητικό και το γνωστό_hash από το αίτημα χρησιμοποιώντας 'certificate' και 'known_hash' ως κλειδιά. Επιστρέψτε 'True' αν το πιστοποιητικό ταιριάζει με το γνωστό_hash και 'False' αλλιώς.
    '''
def verify_certificate_and_hash(certificate, known_hash):
    '''
    Αποκτήστε το πιστοποιητικό και το γνωστό_hash από το αίτημα χρησιμοποιώντας 'certificate' και 'known_hash' ως κλειδιά. Επιστρέψτε 'True' αν το πιστοποιητικό ταιριάζει με το γνωστό_hash και 'False' αλλιώς.
    '''orical
orical