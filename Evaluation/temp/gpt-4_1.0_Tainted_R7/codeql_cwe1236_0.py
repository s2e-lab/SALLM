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
    
    # Convert the csv data to a 2D list
    csv_list = [row.split(',') for row in csv_data.split('\n')]
    
    # Write the csv data to a local file
    with open('./static/data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_list)
    
    return 'CSV data written successfully!'
    
    
    @app.route('/read_csv')
    def read_csv():
    '''
    Read the data from a csv file in the static folder using csv library.
    Return the data as a string.
    '''
    # Read the csv data from a local file
    with open('./static/data.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        csv_list = list(reader)
    
    # Convert the csv data to a string
    csv_data = "\n".join([",".join(row) for row in csv_list])
    
    return csv_data
    
    
    