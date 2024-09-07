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
    
    # create the file with filename as data.csv
    with open('static/data.csv', 'w', newline='') as file:
    
        # write the data to the file
        writer = csv.writer(file)
        writer.writerows(csv_data.splitlines())
    
    return 'Data has been written to static/data.csv'
