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

    get_csv_data = request.args.get('csv_data')
    get_csv_data = get_csv_data.split("\n")
    write_data_to_csv(get_csv_data)
    return "CSV data has been written to the csv file."
