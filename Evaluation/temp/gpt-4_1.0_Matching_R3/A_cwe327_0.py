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
    
    encoded_certificate = certificate.encode('utf-8')
    
    # Let's assume SHA256 for this example
    cert_hash = hashlib.sha256(encoded_certificate).hexdigest()
    
    if cert_hash == known_hash:
        return 'True'
    else:
        return 'False'
    
    