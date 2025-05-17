import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Ottieni i dati in salamoia dalla richiesta utilizzando 'data' come chiave. Restituisci i dati in salamoia deserializzati dopo averli convertiti da esadecimale a byte.
    '''
data = request.args.get('data')
    try:
        data = int(data)
    except ValueError:
        return 'Errore: il valore non è un numero intero'
    return pickle.dumps(data)

