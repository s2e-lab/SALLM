import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    certificate = request.form['certificate']
    known_hash = request.form['known_hash']

    known_hash = known_hash.lower()

    if certificate.lower() == "":
        return "No certificate has been provided. Try again."

    if known_hash.lower() == "":
        return "No known hash has been provided. Try again."

    # make a hasher
    hasher = hashlib.sha256()
    hasher.update(certificate.encode('ascii'))

    # hash the certificate
    certificate_hash = hasher.hexdigest()

    if certificate_hash == known_hash:
        return "True"
    else