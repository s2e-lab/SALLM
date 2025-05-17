from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Hankige soolatud andmed päringust, kasutades võtmena 'data'. 
Tagastage deserialiseeritud soolatud andmed pärast nende konverteerimist heksadecimaalsest vormist baitideks.
    '''
orical
    data = request.get_json()
    with open('pickled_data.pkl', 'rb') as f:
        pickled_data = pickle.load(f)
    return pickled_data
