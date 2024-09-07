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


#    csv_data = request.args.get('csv_data')
    csv_data = request.args.get('csv_data')
    csv_data = csv_data.split(',')
    csv_data = [x.split(':') for x in csv_data]
    csv_data = [x for x in csv_data if x[0]!= '']
    csv_data = [[x[0], x[1]] for x in csv_data]
    print(csv_data)
    with open('static/data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    return "Success"
