import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    certificate = request.args.get('certificate', None)
    known_hash = request.args.get('known_hash', None)
    if certificate is None or known_hash is None:
        return False
    certificate = certificate.encode('ascii')
    calculated_hash = hashlib.sha1(certificate).hexdigest()
    if calculated_hash == known_hash:
        return True
    return False
