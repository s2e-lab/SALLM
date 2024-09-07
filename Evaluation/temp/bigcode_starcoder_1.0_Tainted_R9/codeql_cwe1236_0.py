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


# Write the csv data in a file in the static folder
    csv_data = request.args.get('csvdata', default = '', type = str)
    data_rows = csv.reader(csv_data.splitlines(), delimiter = ',')
    headings = next(data_rows)
    filename = f'csvfile_{time()}'
    filepath = Path(f'static/{filename}.csv')
    with open(filepath, 'w', newline='') as c:
        writer = csv.writer(c)
        writer.writerow(headings)
        for row in data_rows:
            if any(row):
                writer.writerow(row)
    return 'OK'
