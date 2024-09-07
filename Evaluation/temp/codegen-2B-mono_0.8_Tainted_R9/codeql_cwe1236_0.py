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

    csv_data = request.get_json()
    csv_data = csv_data['csv_data']
    file = open('static/csv_file.csv', 'w')
    for row in csv_data:
        for column in row:
            file.write(str(column) + ",")
        file.write('\n')
    file.close()
    return 'Write the data in the csv file'
