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
    
    # Split the data into lines
    lines = csv_data.split("\n")
    data = []
    for line in lines:
        # Split each line into fields and add to data list
        data.append(line.split(","))
    
    # Write the data to a csv file
    with open('static/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    return "CSV data written successfully!"
    
    