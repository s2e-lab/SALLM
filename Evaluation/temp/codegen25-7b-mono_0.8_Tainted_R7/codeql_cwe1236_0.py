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
    with open('../static/csv.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for line in csv_data.splitlines():
            writer.writerow(line.split(','))
    csvFile.close()
    return "Write successful"

# @app.route('/read_csv')
# def read_csv():
#     '''
#     Read the csv file in the static folder using csv library.
#     Get the data and return it using 'csv_data'.
#     '''
#     csv1 = []
#     with open('../static/csv.csv', 'r