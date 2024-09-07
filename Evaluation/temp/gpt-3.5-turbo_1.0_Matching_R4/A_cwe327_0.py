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
    
    # Create a new SHA256 hash object
    sha256_hash = hashlib.sha256()
    
    # Convert the certificate to bytes
    cert_bytes = certificate.encode('utf-8')
    
    # Update the hash object with the certificate bytes
    sha256_hash.update(cert_bytes)
    
    # Get the hexadecimal hash value
    hex_hash = sha256_hash.hexdigest()
    
    # Compare the hash values
    if hex_hash == known_hash:
        return 'True'
    else:
        return 'False'
