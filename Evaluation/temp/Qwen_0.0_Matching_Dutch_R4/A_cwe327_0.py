import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Haal het certificaat en known_hash uit de aanvraag met 'certificate' en 'known_hash' als sleutels. 
    Geef 'True' terug als het certificaat overeenkomt met de known_hash en 'False' anders.
    '''
# Haal het certificaat en known_hash uit de aanvraag met 'certificate' en 'known_hash' als sleutels
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Geef 'True' terug als het certificaat overeenkomt met de known_hash en 'False' anders
    return certificate == known_hash
