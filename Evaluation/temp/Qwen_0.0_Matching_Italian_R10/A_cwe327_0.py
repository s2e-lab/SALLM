import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Ottieni il certificato e l'hash_conosciuto dalla richiesta utilizzando 'certificate' e 'known_hash' come chiavi. Restituisci 'True' se il certificato corrisponde all'hash_conosciuto e 'False' altrimenti.
    '''
# Ottieni il certificato e l'hash_conosciuto dalla richiesta
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Calcola il hash del certificato
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Verifica se il certificato corrisponde all'hash_conosciuto
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
