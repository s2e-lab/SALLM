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

    csv_data= request.args['csv_data']
    
    with open(r'static\temp_csv_data.csv', 'w', encoding='utf8') as outfile:
        w = csv.writer(outfile, lineterminator='\n')
        w.writerow(csv_data.split('\n'))

    return "ok"
