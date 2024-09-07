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

#    csv_data = request.form['csv_data']
    csv_data = request.args.get('csv_data')
    print csv_data
    csv_data = csv_data.replace('\r\n', '\n')
    with open('static/file.csv', 'w') as f:
        f.write(csv_data)
    return csv_data
