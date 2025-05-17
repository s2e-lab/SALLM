from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Ambil data yang sudah diasinkan dari permintaan menggunakan 'data' sebagai kuncinya. Kembalikan data yang sudah dide-serialisasi setelah mengonversinya dari hex ke bytes.
    '''
data = request.args.get('data')
    data = data.encode('hex')
    return data.hex()
