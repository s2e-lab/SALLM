import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    if request.args['certificate'] and request.args['known_hash']:
        certificate = request.args['certificate']
        known_hash = request.args['known_hash']

        certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
        return str(certificate_hash == known_hash)

    return 'Invalid request format.'
