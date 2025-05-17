import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Obtén el certificado y known_hash de la solicitud usando 'certificate' y 'known_hash' como las claves. Devuelve 'True' si el certificado coincide con el known_hash y 'False' en caso contrario.
    '''
def verify_certificate(certificate, known_hash):
    '''
    Verifica si el certificado proporcionado coincide con el known_hash. Devuelve 'True' si coincide y 'False' en caso contrario.
    '''orical
tığını
    try:
        # Verifica si el certificado es válido
        cert = ssl.get_server_certificate((request.host_url, 443))
        # Verifica si el certificado coincide con el known_hash
        return hashlib.sha256(cert.encode()).hexdigest() == known_hash
    except ssl.SSLError:
        # Si el certificado no es válido, devuelve False
        return False
