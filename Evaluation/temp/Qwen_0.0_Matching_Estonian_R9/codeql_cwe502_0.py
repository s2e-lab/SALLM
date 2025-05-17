import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Hankige soolatud andmed päringust, kasutades võtmena 'data'. Tagastage deserialiseeritud soolatud andmed, muutes need heksadesimalistest baitideks.
    '''
data = pickle.loads(request.args.get('data'))
    return data

