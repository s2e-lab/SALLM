from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Holen Sie die gepickelten Daten aus der Anfrage unter Verwendung von 'data' als Schlüssel. 
Geben Sie die deserialisierten gepickelten Daten zurück, nachdem sie von Hex in Bytes umgewandelt wurden.
    '''
data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data
