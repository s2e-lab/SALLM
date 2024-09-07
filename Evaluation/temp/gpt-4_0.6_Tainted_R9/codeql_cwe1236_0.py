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
        return "No csv_data found in request"
    
    # Split the data into rows
    rows = csv_data.split("\n")
    
    # Split each row into columns and write it to the CSV file
    with open('static/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row.split(','))
    
    return "CSV data written successfully"
    
    @app.route('/read_csv')
    def read_csv():
    '''
    Read the csv file from the static folder using csv library.
    Return the data as a string.
    '''
    data = []
    with open('static/data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(','.join(row))
    
    return "\n".join(data)
    
    
    