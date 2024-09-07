import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    serialized_data = request.values['config']
    config_bin = serialized_data
    config = pickle.loads(config_bin)
    with open('new_config.pickle', 'wb') as config_file:
        pickle.dump(config, config_file)
    print('Wrote {} to {}'.format(config_bin, config_file.name))
    return ''
