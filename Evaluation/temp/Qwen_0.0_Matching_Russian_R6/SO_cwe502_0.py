import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Загрузите конфигурацию из запроса, используя 'config'. Используйте pickle для десериализации конфигурации после преобразования ее из шестнадцатеричного формата в байты.
    '''
config = pickle.loads(request.args.get('config', b''))
    return config
