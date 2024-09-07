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

    csv_data = request.args.get('csv_data', '')
    csv_rows = csv_data.split('\n')
    csv_file = 'static/data.csv'
    
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        for row in csv_rows:
            writer.writerow(row.split(','))
    
    # Return the download url of the created data.csv file
    return {'file': f'/static/data.csv'}
    
    
    