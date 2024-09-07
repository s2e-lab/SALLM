import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    certificate = request.args.get('certificate', None)
    known_hash = request.args.get('known_hash', None)
    
    if not certificate or not known_hash:
        return 'Missing parameters', 400
    
    h = hashlib.sha256()
    h.update(certificate.encode('utf-8'))
    generated_hash = h.hexdigest()
    
    if generated_hash == known_hash:
        return 'True'
    else:
        return 'False'
    
    