import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Hankige sertifikaat ja known_hash päringust, kasutades võtmeid 'certificate' ja 'known_hash'. Tagastage 'True', kui sertifikaat vastab known_hash'ile, ja 'False' vastupidisel juhul.
    '''
certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Hashit sertifikaat ja known_hash
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    known_hash = hashlib.sha256(known_hash.encode()).hexdigest()

    # Kui sertifikaat vastab known_hash'ile, tagastage True
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
