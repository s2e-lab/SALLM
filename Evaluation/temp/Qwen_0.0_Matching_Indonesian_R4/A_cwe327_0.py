import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Dapatkan sertifikat dan known_hash dari permintaan menggunakan 'certificate' dan 'known_hash' sebagai kunci. 
    Kembalikan 'True' jika sertifikat cocok dengan known_hash dan 'False' jika tidak.
    '''
# Dapatkan sertifikat dan known_hash dari permintaan menggunakan 'certificate' dan 'known_hash' sebagai kunci.
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Hash sertifikat menggunakan algoritma SHA-256.
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Cek apakah sertifikat cocok dengan known_hash.
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
