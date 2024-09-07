import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    if not request.values.get('certificate') or not request.values.get('known_hash'):
        return 'Certificate and known_hash must be provided.'
    else:
        certificate = request.values.get('certificate')
        known_hash = request.values.get('known_hash')
        return hashlib.sha256(certificate.encode("utf-8")).hexdigest() == known_hash
    
