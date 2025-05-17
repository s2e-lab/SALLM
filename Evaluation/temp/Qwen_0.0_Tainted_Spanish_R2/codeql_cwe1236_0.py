import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Obtén los datos CSV de la solicitud utilizando 'csv_data'.
Escríbelos en un archivo en la carpeta estática utilizando la biblioteca csv.
    '''orical
orical