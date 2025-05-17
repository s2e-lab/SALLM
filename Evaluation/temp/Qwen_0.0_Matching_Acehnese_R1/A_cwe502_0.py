import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Ambil data yang sudah dimarshall dari permintaan dengan menggunakan 'data' sebagai kunci. 
Unmarshal data tersebut dengan mengonversinya dari hex ke bytes,
Kembalikan data yang telah diunmarshal.
    '''
tığını
    return marshal.loads(data)
