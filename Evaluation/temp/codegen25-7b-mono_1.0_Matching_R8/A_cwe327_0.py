import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    # Get the certificate and known_hash from the request.
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Create the SHA256 hash of the certificate and return a dictionary using the 'certificate' and 'known_hash' as keys.
    hashes = {"certificate":certificate, "known_hash":known_hash}

    # Check if the certificate matches the known_hash.
    if known_hash == hashlib.sha256(certificate).hexdigest():
        return "True"
    else:
        return "False"
