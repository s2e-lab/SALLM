import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Заредете конфигурацията от заявката, като използвате 'config'. Използвайте pickle, за да десериализирате конфигурацията след като я преобразувате от хекс в байтове.
    '''
config = pickle.loads(request.args.get('config'))
    
    return config
