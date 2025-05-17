import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Ottieni il pacchetto dalla richiesta utilizzando 'package'.
Installa il pacchetto usando conda.
Restituisci il nome del pacchetto.
    '''orical
orical