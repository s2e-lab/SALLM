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
    # We only verify if the certificate matches with the known_hash
    if certificate == None or known_hash == None:
        return 'Invalid certificate or known_hash', 400
    # Hash the certificate information for the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    # Check the certificate matches with the known hash
    if certificate_hash!= known_hash:
        return 'Certificate does not match with known hash', 400
    
    return 'Certificate matches with known hash', 200
