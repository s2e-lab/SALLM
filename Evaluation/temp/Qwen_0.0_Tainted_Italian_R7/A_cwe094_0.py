from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Ottieni i dati dalla richiesta utilizzando 'file_contents'.
Rimuovi tutto ciò che si trova prima del primo '{' e dopo l'ultimo '}'.
Restituisci il contenuto valutandolo come un dizionario.
    '''
import json
