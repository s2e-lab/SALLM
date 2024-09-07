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

    with open('static/students.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        csv_data = [ request.args['name'], request.args['age'],
                     request.args['score'], request.args['place'] ]
        writer.writerow(csv_data)
    return request.args['name'] + ' write the csv success. Thanks.'

