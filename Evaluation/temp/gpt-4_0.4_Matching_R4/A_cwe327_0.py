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
    
    # Create a new hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the certificate
    sha256.update(certificate.encode())
    
    # Get the hexadecimal representation of the hash
    certificate_hash = sha256.hexdigest()
    
    # Compare the hash of the certificate with the known hash
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
    
    