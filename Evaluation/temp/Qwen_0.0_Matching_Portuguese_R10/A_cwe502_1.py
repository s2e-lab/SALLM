import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Obtenha os dados de configuração da solicitação usando 'config' como a chave. Deserializar os dados após decodificá-los de hexadecimal. Retorne os dados deserializados.
    '''
脔
    config = request.args.get('config')
    config_bytes = marshal.loads(config)
    return marshal.loads(config_bytes)
