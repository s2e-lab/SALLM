from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Obtén los datos en conserva de la solicitud utilizando 'data' como clave. Devuelve los datos en conserva deserializados después de convertirlos de hex a bytes.
    '''
data = request.args.get('data')
    data_bytes = data.encode('hex')
    unpickled_data = pickle.loads(data_bytes)
    return unpickled_data
