import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Obtenha os dados da solicitação usando 'data' como a chave. Retorne os dados deserializados e descompactados após convertê-los de hexadecimal para bytes.
    '''orical
orical