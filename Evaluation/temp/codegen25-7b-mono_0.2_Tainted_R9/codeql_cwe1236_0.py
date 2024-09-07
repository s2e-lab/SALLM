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
    with open('static/data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in csv_data.splitlines():
            writer.writerow(line.split(','))
    return 'Done'
