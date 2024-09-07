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

    # Get the csv data from the request
    csv_data = request.args.get('csv_data')
    
    # Check if csv_data is provided
    if not csv_data:
        return 'No csv data provided', 400
    
    # Write it to a file in the static folder
    with open('static/data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in csv_data.split('\n'):
            csv_writer.writerow(row.split(','))
    
    return 'CSV data written to file successfully', 200
    
    
    