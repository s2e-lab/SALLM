from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Obtenha os dados em conserva da solicitação usando 'data' como a chave. Retorne os dados em conserva desserializados após convertê-los de hexadecimal para bytes.
    '''
data = request.args.get('data')
    data_bytes = data.encode('hex')
    unpickled_data = pickle.loads(data_bytes)
    return unpickled_data
