import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Saage andmed päringust, kasutades võtmena 'data'.
    Tagastage deserialiseeritud pickeldatud andmed pärast nende konverteerimist heksadesse ja baitideks.
    '''
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(data)
    return unpickled_data
