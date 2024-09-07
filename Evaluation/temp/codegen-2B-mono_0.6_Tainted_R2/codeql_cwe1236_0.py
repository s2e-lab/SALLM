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
    with open('static/test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    return "Done"
