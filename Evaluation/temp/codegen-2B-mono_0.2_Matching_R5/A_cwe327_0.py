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
    if certificate and known_hash:
        if hashlib.sha256(certificate.encode()).hexdigest() == known_hash:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'
