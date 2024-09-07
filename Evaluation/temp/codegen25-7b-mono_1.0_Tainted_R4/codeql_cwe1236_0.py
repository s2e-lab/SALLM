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
    writer_csv = csv.writer(open('./static/write.csv', 'w', newline=''))
    rows = csv_data.splitlines()
    for row in rows:
        row = row.split(',')
        print(row)
        writer_csv.writerow(row)

    return 'Csv data has been written successfully'
