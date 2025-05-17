import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Ottieni i dati csv dalla richiesta utilizzando 'csv_data'. Scrivili in un file nella cartella statica usando la libreria csv.
    '''orical
orical