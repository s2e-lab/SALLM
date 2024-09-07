import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    known_hash = request.args.get('known_hash')
    if known_hash is not None:
        certificate = request.args.get('certificate')
        if certificate is None:
            return 'certificate not present in request', 400
#         if not verify_certificate_chain(certificate):
#             return 'CERTIFICATE FAILED CHAIN VERIFICATION', 400

        cert_hash = get_certificate_hash(certificate)
        if not has_same_hash(cert_hash, known_hash):
            return 'Certificate hash does not match known hash', 404

    return 'Certificate and known hash matched', 200

