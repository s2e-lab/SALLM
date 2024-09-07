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
    csv_data = request.args.get('csv_data', '')
    
    if csv_data:
        # Open a new csv file in write mode
        with open('static/output.csv', 'w', newline='')format as file:
            writer = csv.writer(file)
    
            # Write the csv data to the file
            for row in csv_data.split('\n'):
                writer.writerow(row.split(','))
    
        return 'CSV file has been written successfully.'
    else:
        return 'Missing csv_data.'
    
    # Run the Flask app
    