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
    csv_data = csv.reader(csv_data.splitlines())
    with open('csv_test.csv', 'w', newline='') as csvfile:
        for data in csv_data:
            csv.writer(csvfile).writerow(data)
    return 'CSV Data has been saved in the csv_test.csv file'
