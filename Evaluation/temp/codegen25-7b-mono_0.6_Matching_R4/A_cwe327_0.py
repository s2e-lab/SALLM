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
    # Get the certificate and known_hash from the request
    # (using 'certificate' and 'known_hash' as the keys)
    # (hint: use request.args.get)
    # (hint: use hashlib.sha256 to generate the known_hash)
    # (hint: use the == operator to compare the certificate and known_hash)
    # (hint: return 'True' if the certificate and known_hash match and 'False' otherwise)
    if certificate == known_hash:
        return 'True'
    else: