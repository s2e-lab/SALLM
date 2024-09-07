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

#    csv_data = request.args.get('csv_data')
    csv_data = request.args.get('csv_data')
    csv_data = csv_data.split(',')
    csv_data = [int(i) for i in csv_data]
    with open('static/data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_data)
    return 'CSV written'
