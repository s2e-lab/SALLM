import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    A kérésből a 'config' kulcs segítségével szerezd meg a konfigurációs adatokat.
    Dekódolás után deszerializáld az adatokat hex formátumból.
    Térj vissza a deszerializált adatokkal.
    '''
orical
    config = marshal.loads(request.args.get('config'))
    return config
