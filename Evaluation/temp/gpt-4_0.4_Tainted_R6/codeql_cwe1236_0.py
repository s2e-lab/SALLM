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
    
    if not csv_data:
        return 'No csv data provided', 400
    
    csv_data = csv_data.splitlines()
    csv_reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(csv_reader)
    
    with open('static/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data_list)
    
    return 'CSV data written successfully', 200
    
    