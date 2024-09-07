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
    with open('static/data.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['a', 'b', 'c'])
        filewriter.writerow(['1', '2', '3'])
        filewriter.writerow(['4', '5', '6'])
        filewriter.writerow(['7', '8', '9'])
    return 'Done'
