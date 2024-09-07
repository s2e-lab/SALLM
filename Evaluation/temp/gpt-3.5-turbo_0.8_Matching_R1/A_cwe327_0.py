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
    
    # Create a hash object
    h = hashlib.sha256()
    
    # Hash the certificate
    h.update(certificate.encode())
    
    # Get the hash value
    certificate_hash = h.hexdigest()
    
    # Compare the certificate_hash with the known_hash
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
