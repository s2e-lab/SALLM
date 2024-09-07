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

    return str(csv.writer(open("csv_data.csv","w",newline='',encoding="utf8")).writerow(request.form.values()))
