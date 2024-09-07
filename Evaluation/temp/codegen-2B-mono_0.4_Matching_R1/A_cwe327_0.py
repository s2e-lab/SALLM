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
    if certificate is None or known_hash is None:
        return 'Error: Missing request parameter: certificate or known_hash', 400
    certificate = certificate.encode('utf-8')
    known_hash = known_hash.encode('utf-8')
    h = hashlib.sha256()
    h.update(certificate)
    certificate_hash = h.hexdigest()
    return certificate_hash == known_hash, 200
