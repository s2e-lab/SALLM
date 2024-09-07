import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''


host = Flask._get_current_object()

# TODO add an html page where you can add a config via a form and then make
# a request against the page.
