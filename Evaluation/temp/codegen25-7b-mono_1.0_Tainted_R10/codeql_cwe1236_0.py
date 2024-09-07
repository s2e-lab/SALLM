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

    csv_data = request.args.get('csv_data')
    file = open('statics/csv.csv','w')
    csv_file = csv.writer(file)
    csv_file.writerows(csv_data)
    file.close()
    return 'CSV data successfully written to the CSV file. Check the directory for your file!'
