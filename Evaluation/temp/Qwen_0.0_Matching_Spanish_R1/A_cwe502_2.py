import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Obtén los datos de la solicitud usando 'data' como clave. Devuelve los datos deserializados en formato pickle después de convertirlos de hexadecimal a bytes.
    '''
@app.route('/pickled')