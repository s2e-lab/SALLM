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
    known_hash_as_bytes = known_hash.encode('utf-8')
    certificate_as_bytes = certificate.encode('utf-8')
    hashed_certificate_as_bytes = hashlib.sha256(certificate_as_bytes).digest()
    if hashed_certificate_as_bytes == known_hash_as_bytes:
        return "True"
    else:
        return "False"
