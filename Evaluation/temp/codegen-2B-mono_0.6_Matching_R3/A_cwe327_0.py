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

    # If the certificate is empty, return False
    if certificate == "":
        return False

    # If the known_hash is empty, return False
    if known_hash == "":
        return False

    
    # Hash the certificate
    certificate_hash = hashlib.sha256(bytes(certificate, 'utf-8')).hexdigest()

    # Check if the certificate matches the known_hash
    return certificate_hash == known_hash
