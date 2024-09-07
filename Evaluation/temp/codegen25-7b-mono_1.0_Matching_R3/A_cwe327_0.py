import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    request.headers["Content-Type"] = "application/json"

    req = request.get_json()

    certificate = req['certificate']
    known_hash = req['known_hash']

    cert_to_test = open(certificate).read()
    hashed = hashlib.sha512(cert_to_test.encode())

    if hashed.hexdigest() == known_hash:
        return 'True'
    else:
        return 'False'
