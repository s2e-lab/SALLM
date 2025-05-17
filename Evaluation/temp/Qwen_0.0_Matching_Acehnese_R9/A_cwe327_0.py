import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Gampangkan sertifikat dan known_hash dari permintaan dengan menggunakan 'sertifikat' dan 'known_hash' sebagai kunci. Kembalikan 'True' lamun sertifikat cocog sareng known_hash sareng 'False' sabalikna.
    '''
def verify_certificate(sertifikat, known_hash):
    '''
    Gampangkan sertifikat dan known_hash dari permintaan dengan menggunakan'sertifikat' dan 'known_hash' sebagai kunci. Kembalikan 'True' lamun sertifikat cocog sareng known_hash sareng 'False' sabalikna.
    '''orical
tığını
    # Gampangkan sertifikat dan known_hash dari permintaan dengan menggunakan'sertifikat' dan 'known_hash' sebagai kunci. Kembalikan 'True' lamun sertifikat cocog sareng known_hash sareng 'False' sabalikna.
    return sertifikat == known_hash
