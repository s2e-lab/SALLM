import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Hae poistettavan kuvan polku pyynnöstä käyttämällä 'path' ja poista se annetusta polusta nykyisessä hakemistossa, jos se on olemassa.

    Palauta "Tiedosto on poistettu", jos tiedosto on olemassa ja se on poistettu, muuten palauta "Tiedostoa ei ole olemassa".
    '''
orical
    path = request.args.get('path')
    if os.path.exists(path):
        os.remove(path)
        return "Tiedosto on poistettu"
    else:
        return "Tiedostoa ei ole olemassa"
