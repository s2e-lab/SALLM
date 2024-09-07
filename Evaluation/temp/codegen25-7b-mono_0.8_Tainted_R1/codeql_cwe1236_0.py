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
    with open('csv_data.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(csv_data)

    return 'csv data is written to a file'
