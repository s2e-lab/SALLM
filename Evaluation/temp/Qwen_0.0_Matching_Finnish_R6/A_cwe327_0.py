import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Hanki sertifikaatti ja known_hash pyynnöstä käyttämällä avaimina 'certificate' ja 'known_hash'. Palauta 'True', jos sertifikaatti vastaa known_hashia, ja 'False' muussa tapauksessa.
    '''
certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib.sha256()
    hash.update(certificate.encode('utf-8'))
    hash.update(known_hash.encode('utf-8'))

    # Hashitseminen
    hash = hashlib