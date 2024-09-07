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

    # get the csv data from the request
    csv_data = request.args.get('csv_data')
    # write the csv data to a file
    with open('static/csv_file.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_data.split('\n'))
    return 'csv data written'

