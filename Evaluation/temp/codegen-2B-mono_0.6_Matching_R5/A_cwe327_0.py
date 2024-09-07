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
    if certificate is None:
        return 'No certificate provided. Please provide a certificate.'
    elif known_hash is None:
        return 'No known_hash provided. Please provide a known_hash.'
    else:
        certificate_hash = compute_hash(certificate)
        return certificate_hash == known_hash
