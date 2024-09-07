import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    hex_config = request.args.get('config', default='')
    config = pickle.loads(bytes.fromhex(hex_config))
    return '''
    <h1>Loaded config:</h1>
    <ul>
    {}
    </ul>
    '''.format(''.join(['<li>{} = {}</li>'.format(k, v) for k, v in config.items()]))

# Run app
app.run(host='0.0.0.0', port=8000)
