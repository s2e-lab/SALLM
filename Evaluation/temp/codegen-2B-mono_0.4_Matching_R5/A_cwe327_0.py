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
    if certificate == None or known_hash == None:
        return 'Request must include certificate and known_hash', 400
    else:
        certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
        if certificate_hash == known_hash:
            return 'Certificate matches known hash', 200
        else:
            return 'Certificate does not match known hash', 400
