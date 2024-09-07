import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''

    cert_data = request.args.get('certificate', type = str)
    known_hash = request.args.get('known_hash', type = str)
    digest = hashlib.sha1()
    digest.update(cert_data)
    received_hash = digest.hexdigest()
    return received_hash == known_hash

