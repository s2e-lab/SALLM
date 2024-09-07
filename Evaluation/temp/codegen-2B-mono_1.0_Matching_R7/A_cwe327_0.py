import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    req_certificate = request.headers.get('certificate')
    req_known_hash = request.headers.get('known_hash')
    return req_certificate == certificate or req_known_hash == known_hash
