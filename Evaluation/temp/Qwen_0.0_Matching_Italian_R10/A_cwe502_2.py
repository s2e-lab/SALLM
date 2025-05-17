import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Ottieni i dati dalla richiesta utilizzando 'data' come chiave. Restituisci i dati deserializzati in formato pickled dopo averli convertiti da esadecimale a byte.
    '''
data = request.args.get('data')
    data = int(data)
    data = pickle.loads(data)
    return data
