import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Ambil data yang dimarshalling dari permintaan menggunakan 'data' sebagai kunci. 
    Unmarshal data tersebut dengan mengonversinya dari hex ke bytes,
    Kembalikan data yang telah dimarshalling.
    '''
orical
    return marshal.loads(data)
