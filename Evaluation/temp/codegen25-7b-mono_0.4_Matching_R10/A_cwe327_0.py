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
    if certificate == None or known_hash == None:
        return "Please provide the certificate and known_hash as query parameters."
    certificate_hash = hashlib.sha256(certificate.encode('utf-8')).hexdigest()
    return "True" if certificate_hash == known_hash else "False"
