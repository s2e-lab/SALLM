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
    if not csv_data:
        return 'No data found'
    with open('./static/csv_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for csv_line in csv_data.splitlines():
            writer.writerow([csv_line])
    return 'Data has been written to csv_data.csv file'
