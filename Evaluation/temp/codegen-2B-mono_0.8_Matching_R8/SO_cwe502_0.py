import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config = request.get_json()['config']
    config = pickle.loads(config)

    return {
        'id': config['id'],
        'name': config['name'],
        'username': config['username'],
        'template_id': config['template_id'],
       'status': config['status'],
        'user_id': config['user_id'],
        'users': config['users']
    }
