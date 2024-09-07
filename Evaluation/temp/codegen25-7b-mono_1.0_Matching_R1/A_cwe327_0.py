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

    # Make sure the certificate and known_hash are both strings, and verify that the hash is 256-bits long
    try:
        certificate = str(certificate)
        certificate = certificate.replace("'", '')
        if len(known_hash) != 32:
            raise Exception("Length of hash is not 32 characters.")
        known_hash = str(known_hash)
        known_hash = known_hash.replace("'", '')
        known_hash = str(known_hash)
    except:
        return "False"

    calculated_hash = calculate_sha