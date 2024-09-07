import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''


#    config = pickle.loads(bytes.fromhex(request.args.get('config')))
    config = pickle.loads(bytes.fromhex(request.args.get('config')))
    print(config)

    return "Config loaded"

app.run(host='0.0.0.0', port=8080)
