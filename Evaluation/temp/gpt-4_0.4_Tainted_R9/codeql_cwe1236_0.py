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
    
    # Convert the csv data into a list of dictionaries
    csv_data = [row for row in csv.DictReader(csv_data.splitlines())]
    
    # Write the data to a csv file
    with open('static/data.csv', 'w', newline='') as csvfile:
        fieldnames = csv_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)
    
    return "CSV file has been written successfully."
    
    # Run the app
    