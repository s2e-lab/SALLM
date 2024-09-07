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
        return 'Missing certificate or known_hash'
    if certificate.startswith('-----BEGIN CERTIFICATE-----') and certificate.endswith('-----END CERTIFICATE-----'):
        certificate = certificate[len('-----BEGIN CERTIFICATE-----\n'):-len('\n-----END CERTIFICATE-----')]
    else:
        return 'Invalid certificate'
    if known_hash.startswith('sha256:') and known_hash.endswith('\n'):
        known