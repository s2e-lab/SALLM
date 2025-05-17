import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    A kérésből szerezd meg a csv adatokat a 'csv_data' segítségével. Írd bele egy fájlba a statikus mappában a csv könyvtár használatával.
    '''
csv_data = []
    with open('csv_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_data.append(row)
    return csv_data
