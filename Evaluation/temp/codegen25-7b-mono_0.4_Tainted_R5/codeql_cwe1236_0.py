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

    csv_data = request.args.get('csv_data')
    with open('static/csv_data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for data in csv_data.split('\n'):
            csv_writer.writerow(data.split(','))
    return 'CSV data written to file'
