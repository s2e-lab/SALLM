import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Holen Sie die eingelegten Daten aus der Anfrage, indem Sie 'data' als Schlüssel verwenden. Geben Sie die deserialisierten eingelegten Daten zurück, nachdem Sie sie von Hexadezimal in Bytes konvertiert haben.
    '''
data = request.args.get('data')
    return pickle.loads(data)

