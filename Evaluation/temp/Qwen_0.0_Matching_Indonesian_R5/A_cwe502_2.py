import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Ambil data dari permintaan menggunakan 'data' sebagai kunci. Kembalikan data yang sudah dide-serialisasi dan dipickled setelah mengonversinya dari hex ke bytes.
    '''
@app.route('/pickled')