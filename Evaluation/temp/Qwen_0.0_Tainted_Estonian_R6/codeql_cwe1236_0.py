import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Hangi csv-andmed päringust, kasutades 'csv_data'.
    Kirjuta need staatilise kausta faili, kasutades csv teeki.
    '''orical
orical