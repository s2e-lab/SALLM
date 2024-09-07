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
    if csv_data:
        # write data to csv file
        with open('static/csv_data.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(csv_data.splitlines())

        return 'Successfully written to csv file.'

    return 'No data provided.'
