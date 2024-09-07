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
    
    # Split the data into rows
    csv_rows = csv_data.split('\n')
    
    # Open a csv file in write mode
    with open('static/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
    
        # Write each row to the csv file
        for row in csv_rows:
            writer.writerow(row.split(','))
    
    return 'CSV file has been written successfully.'
    
    # Run the app
    