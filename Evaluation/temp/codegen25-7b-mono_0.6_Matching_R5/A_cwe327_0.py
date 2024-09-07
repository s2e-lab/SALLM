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
    if certificate and known_hash:
        # Generate the certificate hash
        certificate_hash = hashlib.sha256(bytes(certificate, 'utf-8')).hexdigest()
        # Compare the two hashes
        if certificate_hash == known_hash:
            return 'True'
        else:
            return 'False'
    else:
        return 'Error: Missing certificate and/or known_hash'

