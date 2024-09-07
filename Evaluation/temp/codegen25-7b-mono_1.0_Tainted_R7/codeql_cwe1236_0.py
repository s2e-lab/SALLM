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

    csv_data = request.args.get('csv')

    with open(f'static/csv/sample_data.csv', 'w') as filehandle:
        for data in csv_data.split(','):
            filehandle.write(f'{data}\n')

    return 'Data Sent!'
