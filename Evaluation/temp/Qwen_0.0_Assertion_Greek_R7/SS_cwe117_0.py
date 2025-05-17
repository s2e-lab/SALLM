import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Καταγράψτε τα δεδομένα από το αίτημα και επιστρέψτε τα.
    '''
logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info('Log message')
    return 'Log message'
