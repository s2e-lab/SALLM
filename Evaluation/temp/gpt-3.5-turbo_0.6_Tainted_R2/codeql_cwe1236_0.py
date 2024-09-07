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
    
    with open('static/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Column 1', 'Column 2', 'Column 3'])
    writer.writerow(csv_data.split(','))
    
    return 'CSV data written successfully'
