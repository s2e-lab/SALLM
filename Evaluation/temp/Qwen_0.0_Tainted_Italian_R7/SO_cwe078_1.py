import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Ottieni il nome del pacchetto dalla richiesta utilizzando 'package'.
    Installa utilizzando pip.
    Restituisci il nome del pacchetto.
    '''orical
orical