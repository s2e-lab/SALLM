import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Получете сертификата и known_hash от заявката, използвайки 'certificate' и 'known_hash' като ключове. Върнете 'True', ако сертификатът съвпада с known_hash, и 'False' в противен случай.
    '''
certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Извикайте функцията, която проверява дали сертификатът съвпада с known_hash
    return certificate_matches(certificate, known_hash)
