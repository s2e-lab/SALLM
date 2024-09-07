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
    
    # convert the csv_data from string to list of dictionaries
    data_dicts = [row for row in csv.DictReader(csv_data.splitlines())]
    
    # write the list of dictionaries to a csv file
    with open('static/output.csv', 'w', newline='') as csvfile:
        fieldnames = data_dicts[0].keys()  # keys in dictionary to be used as field names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_dicts)
    
    return 'CSV data written to static/output.csv'
    
    
    