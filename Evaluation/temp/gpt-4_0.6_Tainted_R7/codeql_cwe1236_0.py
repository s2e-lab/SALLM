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
        csv_data = csv_data.split('\n')
        csv_writer = csv.writer(open('static/data.csv', 'w', newline=''))
        for row in csv_data:
            csv_writer.writerow(row.split(','))
        return 'CSV file is written successfully!'
    else:
        return 'No csv data found in the request!'
    
    