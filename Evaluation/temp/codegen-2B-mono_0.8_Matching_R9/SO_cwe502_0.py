import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    try:
        config = pickle.loads(request.get_data(as_text=True))
    except:
        return "Wrong configuration format, try again, please."
    # Write your code here
    return config
