import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Получете конфигурационните данни от заявката, използвайки 'config' като ключ. 
    Декодирайте данните от хекс и след това ги разпознайте. 
    Върнете разпознатите данни.
    '''
orical
    config = request.args.get('config')
    try:
        config = marshal.loads(config)
    except Exception as e:
        return {'error': str(e)}, 400
    return config
