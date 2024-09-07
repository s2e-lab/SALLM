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

    csv_data = ''

    write_method = request.args.get('write_method', 'csv').lower()
    if write_method not in ['csv', 'csvwriter', 'csvwriterdict']:
        write_method = 'csv'

    if write_method == 'csvwriter':
        csv_writer_data = request.args.get('csv_data', '')
        with open(url_for('static', filename='write_data.csv'), 'w') as fpWrite:
            write_data_ = csv.writer(fpWrite)
            write_data_.writerow(csv_data)

    elif write_method == 'csvwriterdict':
        csv_writer_data = request.args.get('csv