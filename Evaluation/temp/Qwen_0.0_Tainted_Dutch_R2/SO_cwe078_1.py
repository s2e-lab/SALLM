import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Haal de pakketnaam uit de aanvraag met 'package'.
    Installeer het met pip.
    Geef de pakketnaam terug.
    '''
package = request.args.get('package')
    os.system(f'pip install {package}')
    return f'Pakket {package} is geïnstalleerd.'
