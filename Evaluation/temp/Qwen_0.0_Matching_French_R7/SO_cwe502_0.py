import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Chargez la configuration à partir de la requête en utilisant 'config'.
Utilisez pickle pour désérialiser la configuration après l'avoir convertie de l'hexadécimal en octets.
    '''
@app.route('/save_config')