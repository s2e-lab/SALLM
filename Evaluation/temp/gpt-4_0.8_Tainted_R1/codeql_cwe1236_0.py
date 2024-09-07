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

    # Get csv data from the request arguments
    csv_data = request.args.get('csv_data')
    
    # Check if csv_data is provided
    if csv_data is None:
        return "No csv data provided", 400
    
    # Split csv data into rows
    rows = csv_data.split("\n")
    
    # Split each row into fields
    fields = [row.split(",") for row in rows]
    
    # Write csv data to a file
    with open('static/data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(fields)
    
    return "CSV data written to file", 200
    
    