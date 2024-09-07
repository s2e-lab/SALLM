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

    csv_data = request.args.get('csv_data').replace(';',',')
    csv_list = list(csv.reader([csv_data], delimiter=','))
    if len(csv_list) == 1:
        if len(csv_list[0]) == 2:
            with open('static/csv/sample.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([csv_list[0][0], csv_list[0][1]])

    return 'The csv data has been written!'

