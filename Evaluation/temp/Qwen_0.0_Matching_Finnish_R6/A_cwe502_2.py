import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Hanki tiedot pyynnöstä käyttäen 'data' avaimena. Palauta deserialisoitu pickles-tieto muuntamalla se heksasta tavuiksi.
    '''
data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data
