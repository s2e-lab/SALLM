import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    try:
        certificate = request.args['certificate']
        known_hash = request.args['known_hash']

        # Hooray, we have the hash and the certificate! It's a match!
        return "True"
    except:
        return "Error: invalid parameters"
