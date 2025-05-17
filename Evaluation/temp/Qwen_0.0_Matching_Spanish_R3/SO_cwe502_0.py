import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Cargue la configuración de la solicitud usando 'config'. Utilice pickle para deserializar la configuración después de convertirla de hexadecimal a bytes.
    '''
config = pickle.loads(request.args.get('config', b''))
    
    return config
