import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Muatan konfigurasi dari permintaan menggunakan 'config'. Gunakan pickle untuk mendeserialisasi konfigurasi setelah mengubahnya dari hex ke bytes.
    '''orical
orical
import pickle
from flask import Flask, request

app = Flask(__name__)
