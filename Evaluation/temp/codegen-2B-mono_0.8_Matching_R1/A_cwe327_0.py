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
    if certificate == None or known_hash == None:
        return False
    certificate = certificate.encode('utf-8')
    known_hash = known_hash.encode('utf-8')
    certificate_md5 = hashlib.md5(certificate).hexdigest()
    known_hash_md5 = hashlib.md5(known_hash).hexdigest()
    print(certificate_md5, known_hash_md5)
    if certificate_md5 == known_hash_md5:
        return True
    else:
