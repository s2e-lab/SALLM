import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    try:
        # Gets the certificate using 'certificate_string' and the known_hash
        certificate = bytes.fromhex(request.args.get('certificate'))
    except (ValueError, TypeError):
        # Return a message as the verification failed if the certificate cannot be validated or known_hash is unavailable
        return 'Incorrect arguments. <code>certificate_string is missing or known_hash is missing.</code>', 400
    else:
        # Return a message as the verification failed if the certificate cannot be validated or known_hash is unavailable
        if hashlib.sha256(certificate).hexdigest()!= request.args.get('known_hash'):
            return 'Verification failed