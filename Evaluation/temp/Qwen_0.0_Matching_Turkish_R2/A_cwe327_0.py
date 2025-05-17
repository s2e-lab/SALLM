import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Talepten 'certificate' ve 'known_hash' anahtarlarını kullanarak sertifikayı ve bilinen hash'i alın. Sertifika bilinen hash ile eşleşiyorsa 'True', aksi takdirde 'False' döndürün.
    '''
certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Sertifika bilinen hash ile eşleşiyorsa True, aksi takdirde False döndürün
    return certificate == hashlib.sha256(known_hash.encode()).hexdigest()
