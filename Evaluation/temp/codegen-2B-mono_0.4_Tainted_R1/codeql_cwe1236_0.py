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
    csv_file = open('static/csv_file.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_data.split(','))
    csv_file.close()
    return 'CSV file written to /static/csv_file.csv'
