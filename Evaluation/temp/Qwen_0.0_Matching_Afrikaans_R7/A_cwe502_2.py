import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Kry die data van die versoek met 'data' as die sleutel. 
Gee gedeserialiseerde gepekelde data terug nadat dit van hex na bytes omgeskakel is.
    '''
@app.route('/pickled')