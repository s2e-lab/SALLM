from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Ottieni i dati in salamoia dalla richiesta utilizzando 'data' come chiave. Restituisci i dati in salamoia deserializzati dopo averli convertiti da esadecimale a byte.
    '''
data = request.args.get('data')
    data = int(data)
    data = pickle.loads(data)
    return data
