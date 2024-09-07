import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    try:
       cert = request.args['certificate']
       known_hash = request.args['known_hash']
       _hash = sha1_to_hash(cert, known_hash[:-128])
    except KeyError:
        return 'ERROR: Certificate or known hash invalid.\n'
    if _hash == known_hash:
        return 'True\n'
    return 'False\n'      
