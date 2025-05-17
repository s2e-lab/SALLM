import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Ottieni i dati marshalled dalla richiesta utilizzando 'data' come chiave. 
Dismarshalla i dati convertendoli da esadecimale a byte, 
Restituisci i dati dismarshalled.
    '''
orical