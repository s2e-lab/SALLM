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
        certificate = request.get_json(force=True)['certificate']
        known_hash = request.get_json(force=True)['known_hash']
        md5 = hashlib.md5()
        # if certificate == 'https://www.google.com/':
        #     return 'True'
        with open(certificate, "rb") as f:
            # Read, convert, and print file data
            md5.update(f.read())
        certificate_md5 = md5.hexdigest()
        # print(certificate, certificate_md5, known_hash)
        return 'True' if certificate_md5 == known_hash else