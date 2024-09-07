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

    with app.test_request_context():
        csv_data = request.get_json()
        csv_data_keys = list(csv_data.keys())

        #check if the csv data was provided to the endpoint.
        if ('header' in csv_data_keys) and ('data' in csv_data_keys):
            header = dict(csv_data['header'])
            data = list(csv_data['data'])
            
            # check if correct types of the csv data.
            try:
                header = dict(map(int, header.keys()))
                data = list(map(int, data))
            except:
                return 'Incorrect types of CSV data.'
            
            # Check if header