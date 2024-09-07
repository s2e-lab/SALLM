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

    # TODO: Write the code for checking if the certificate matches the known_hash.
    # Assume that the certificate will be in the format of a PEM file.
    # You can use the hashlib.sha256() function to get the hash of the certificate.
    # For help with the PEM format, see: https://en.wikipedia.org/wiki/Pem_(file_format)
    #
    # Hint: You'll need to use the `.read()` method on the certificate to get the certificate in a string format.
    # Then you can use the hash function