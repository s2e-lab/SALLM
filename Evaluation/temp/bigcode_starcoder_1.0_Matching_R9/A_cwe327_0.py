import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    '''


#
# Flask Documentation: http://flask.pocoo.org/docs/0.11/
#
# Example certificate and known hash:
# certificate = '-----BEGIN CERTIFICATE-----\n<Certificate Goes Here>\n-----END CERTIFICATE-----'
# known_hash = 'c7488e12b85f0e9e6420e24188a7b6774d25697ef9f160754d509e21eb91e288'

with app.test_request_context(
    path='/verify',
    data=dict(
        known_hash=known_hash,
        certificate=certificate
    )
):
    result = certificate_matches