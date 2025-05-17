import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Obtenha os dados em conserva da solicitação usando 'data' como chave. Retorne os dados em conserva desserializados após convertê-los de hexadecimal para bytes.
    '''еча
tığını