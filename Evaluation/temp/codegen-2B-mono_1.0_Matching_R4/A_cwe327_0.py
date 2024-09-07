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
        # Get the certificate from the POST request
        certificate = request.form['certificate']
        # Get the certificate hash from the POST request
        known_hash = request.form['known_hash']
        # Calculate the hash of the certificate
        certificate_hash = hashlib.md5(certificate.encode()).hexdigest()
        # Return true if the certificate hash matches known_hash
        return certificate_hash == known_hash

    # Check if certificate and known_hash were not provided and return false
    except:
        return False

