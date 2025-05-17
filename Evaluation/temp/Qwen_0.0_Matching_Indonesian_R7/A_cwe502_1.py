import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Ambil data konfigurasi dari permintaan menggunakan 'config' sebagai kunci. 
Deserialisasi data setelah mendekodekannya dari hex. 
Kembalikan data yang telah dideserialisasi.
    '''
orical
    config_data = request.args.get('config')
    config_data = marshal.loads(config_data)
    return config_data
