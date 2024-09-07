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
    
    # Create a list of rows from csv_data with each field as a separate item in the sub-list
    rows = [row.split(',') for row in csv_data.split('\n')]
    
    with open('static/output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    return "CSV file has been written successfully"
    
    # Run the app
    