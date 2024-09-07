import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    if request.headers.get('certificate') and request.headers.get('known_hash'):
        certificate = request.headers.get('certificate')
        known_hash = request.headers.get('known_hash')
        certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
        if certificate_hash == known_hash:
            return True
        else:
            return False
    else:
        return '', 400
        