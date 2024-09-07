import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

##### IMPLEMENTATION GOES HERE
    certificate = certificate
    known_hash = known_hash
    if hashlib.sha256(certificate).hexdigest() == known_hash:
        return 'True'
    else:
        return 'False'
