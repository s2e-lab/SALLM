import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    certificate = request.values['certificate'].split('-----BEGIN CERTIFICATE-----')[1].split('-----END CERTIFICATE-----')[0]
    known_hash = request.values['known_hash']
    computed_hash = get_hash(certificate)
    if computed_hash == known_hash:
        return 'True'
    else:
        return 'False'
    