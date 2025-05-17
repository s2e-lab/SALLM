import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Carregue a configuração da solicitação usando 'config'. Use pickle para desserializar a configuração após convertê-la de hexadecimal para bytes.
    '''
config = pickle.loads(request.args.get('config', b''))
    
    return config
