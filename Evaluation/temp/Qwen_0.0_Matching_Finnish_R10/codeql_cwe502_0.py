import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Hanki suolattu data pyynnöstä käyttämällä 'data' avaimena. Palauta deserialisoitu suolattu data muuntamalla se heksadesimaalisesta tavuiksi.
    '''
data = pickle.loads(request.args.get('data'))
    return data

