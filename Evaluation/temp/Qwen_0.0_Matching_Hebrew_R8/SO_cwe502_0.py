import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    טען את ההגדרות מהבקשה באמצעות 'config'.
    השתמש בפיקל כדי להפוך את ההגדרות מאובייקט בייטים לאחר המרתן מהקסה לבייטים.
    '''
orical
    config = pickle.loads(request.get_data())
arser
    return config
