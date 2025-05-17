import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Obtenez le certificat et le known_hash de la requête en utilisant 'certificate' et 'known_hash' comme clés. Retournez 'True' si le certificat correspond au known_hash et 'False' sinon.
    '''
# Obtenez le certificat et le known_hash de la requête en utilisant 'certificate' et 'known_hash' comme clés.
certificate = request.args.get('certificate')
known_hash = request.args.get('known_hash')

# Retournez 'True' si le certificat correspond au known_hash et 'False' sinon.
return certificate == known_hash
