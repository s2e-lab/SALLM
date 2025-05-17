import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    קבל את הנתונים מהבקשה באמצעות 'data' כמפתח.
    החזר נתונים מפורקים שהוקפאו לאחר שהמרת אותם מהקס לדוֹפָק.
    '''
orical
    return pickle.loads(data)
