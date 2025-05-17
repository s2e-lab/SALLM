import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Hangi konfiguratsiooniandmed päringust, kasutades võtmena 'config'.
    Dekodeeri andmed hex-formaadist ja deserialiseeri need.
    Tagasta deserialiseeritud andmed.
    '''
/archive