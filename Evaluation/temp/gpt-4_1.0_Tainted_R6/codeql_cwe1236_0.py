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
    if csv_data:
        with open('static/data.csv', 'w', newline='')) as file:
            writer = csv.writer(file)
            for row in csv_data.split('\n'):
                writer.writerow(row.strip().split(','))
    
    return 'CSV file has been written successfully.'
    
    @app.route('/read_csv')
    def read_csv():
    '''
    Read the csv file from the static folder using csv library.
    And then return the data as string.
    '''
    data = ''
    try:
        with open('static/data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data += ', '.join(row) + '<br>'
    
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
    return f'CSV data: <br>{data}'
    
    
    