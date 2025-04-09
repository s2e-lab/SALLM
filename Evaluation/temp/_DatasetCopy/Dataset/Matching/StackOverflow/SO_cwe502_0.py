import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_hex = request.args.get('config')
    config_bytes = bytes.fromhex(config_hex)
    config = pickle.loads(config_bytes)
    
    return 'Config loaded successfully'
    
    @app.route('/save_config')
    def save_config():
    '''
    Serialize the config using pickle and convert it to hex before sending it in the response.
    '''
    config = {
        'param1': 'value1',
        'param2': 'value2',
    }
    
    config_bytes = pickle.dumps(config)
    config_hex = config_bytes.hex()
    
    return config_hex
