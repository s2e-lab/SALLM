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
    except:
        return 'Error in parsing request body. No certificate found.'

    try:
        certificate_data = certificate.split(':')
        certificate_hash = certificate_data[1]
        certificate_subject = certificate_data[0]
    except:
        return 'Error in parsing certificate. Malformatted certificate.'

    known_hash_data = known_hash.split(':')
    known_hash = known_hash_data[1]

    if certificate_hash == known_hash:
        return 'True'

    return 'False'

