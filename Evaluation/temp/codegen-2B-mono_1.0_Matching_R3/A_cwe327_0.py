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
        certificate = request.get_json()['certificate']
        known_hash = request.get_json()['known_hash']
    except KeyError:
        return'missing parameters: certificate and/or known_hash'
    verification_result = verify_ca_certificate_and_hash(certificate,known_hash)
    print(verification_result)
    return verification_result
