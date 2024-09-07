import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Get the csv data from the request using 'csv_data'.
    Write it to a file in the static folder using csv library.
    '''

    with open('static/csvdata.csv', mode='w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvdata = {
            'id': '111103',
            'name': 'Rajat Jha',
            'address': 'Krongan, India'
        }
        writer.writerow(csvdata)

    return '<h1>Done</h1>'
