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
    if csv_data is None:
        return 'No data provided', 400
    
    # Split the data into rows
    rows = csv_data.split('\n')
    
    # Split each row into fields
    rows = [row.split(',') for row in rows]
    
    # Write the data to a csv file
    with open('static/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    return 'Data written to csv file', 200
    
    