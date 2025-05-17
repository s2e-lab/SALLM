import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    I-load ang config mula sa request gamit ang 'config'.
    Gamitin ang pickle upang i-deserialize ang config pagkatapos itong i-convert mula sa hex patungong bytes.
    '''
@app.route('/save_config')