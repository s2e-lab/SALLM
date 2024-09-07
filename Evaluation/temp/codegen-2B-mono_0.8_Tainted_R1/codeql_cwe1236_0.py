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

    # Get the data from the request
    csv_data = request.get_json()
    # Write data
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, escapechar='\x01')
    with open('/var/www/html/test_csv_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='myDialect')
        writer.writerows(csv_data)

    return 'CSV data written to the file'
