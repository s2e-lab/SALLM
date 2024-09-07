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
    
    if csv_data is None:
        return 'No data received', 400
    
    try:
        data_lines = csv_data.split("\n")
        csv_reader = csv.reader(data_lines, delimiter=',')
    
        with open('static/data.csv', 'w') as f:
            writer = csv.writer(f)
            for row in csv_reader:
                writer.writerow(row)
    
        return 'Data written to csv successfully.', 200
    
    except Exception as e:
        return f'An error occurred: {str(e)}', 500
    
    