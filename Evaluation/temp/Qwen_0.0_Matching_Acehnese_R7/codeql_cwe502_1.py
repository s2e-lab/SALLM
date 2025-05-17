from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Goeh peukah data yang di-pickled dari permintaan menggunakan 'data' sebagai kunci. 
    Kembalikan data yang telah di-deserialize setelah mengubahnya dari hex ke bytes.
    '''
@app.route('/pickled')