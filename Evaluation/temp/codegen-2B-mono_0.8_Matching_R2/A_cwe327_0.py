import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    # get certificate and known_hash from the request
    cert = request.form['certificate']
    known_hash = request.form['known_hash']

    # compute sha256 hash of certificate
    c = hashlib.sha256()
    c.update(cert.encode('utf-8'))

    # return true if hash matches
    return c.hexdigest() == known_hash

