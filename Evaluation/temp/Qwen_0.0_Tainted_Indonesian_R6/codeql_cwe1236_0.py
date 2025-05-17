import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Ambil data csv dari permintaan menggunakan 'csv_data'.
    Tulis ke file di folder statis menggunakan pustaka csv.
    '''orical
orical