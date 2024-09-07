import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    if certificate is None or known_hash is None:
        return 'Could not verify certificate. Please provide both a certificate and a known_hash.'

    # Check if the certificate matches the known_hash.
    if certificate_matches(certificate, known_hash):
        return 'True'
    return 'False'
