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
    csv_lines = csv_data.split('\n')
    
    with open('static/data.csv', 'w', newline='')) as file:
        writer = csv.writer(file)
        for line in csv_lines:
            writer.writerow(line.split(','))
    
    return 'CSV data written successfully!'
    
    