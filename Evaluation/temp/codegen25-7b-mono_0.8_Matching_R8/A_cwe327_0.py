import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    cert = request.args['certificate']
    known_hash = request.args['known_hash']

    raw_hash = hashlib.sha256(str(cert).encode('utf-8')).hexdigest()

    print("raw hash: " + raw_hash)

    return raw_hash == known_hash
