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
    
    # Convert the certificate into bytes
    certificate_bytes = bytes(certificate, 'utf-8')
    
    # Create a new sha256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the certificate bytes
    hash_object.update(certificate_bytes)
    
    # Get the hexadecimal representation of the hash
    certificate_hash = hash_object.hexdigest()
    
    # Compare the certificate_hash with the known_hash
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
    
    
    