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

    try:
        assert certificate and known_hash
        assert certificate.count('-----') == 4
    except:
        raise AssertionError(
            'Malformed certificate or known_hash'
        )

    # Get the certificate's SHA256 hash
    sha256_hash = get_sha256_hash(certificate)

    if sha256_hash == known_hash:
        return True
    else:
        return False
