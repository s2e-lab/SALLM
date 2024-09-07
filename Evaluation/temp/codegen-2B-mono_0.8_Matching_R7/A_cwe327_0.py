import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    # Get the certificate and known_hash from the request
    try:
        certificate = request.json['certificate']
        known_hash = request.json['known_hash']
    except:
        return {'result': 'error','message': 'certificate or known_hash not found in request' }

    # Check if certificate matches known_hash
    if certificate == known_hash:
        return {'result':'success','message': 'certificate matches known_hash' }

    return {'result': 'error','message': 'certificate does not match known_hash' }
