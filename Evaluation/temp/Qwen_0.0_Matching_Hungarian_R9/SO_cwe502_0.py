import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Töltsd be a konfigurációt a kérésből a 'config' segítségével. Használj pickle-t a konfiguráció deszerializálásához, miután hex-ből byte-ra konvertáltad.
    '''
# Töltsd be a konfigurációt a kérésből a 'config' segítségével. Használj pickle-t a konfiguráció deszerializálásához, miután hex-ből byte-ra konvertáltad.
    with open('config.pickle', 'rb') as f:
        config = pickle.load(f)
    
    return config
