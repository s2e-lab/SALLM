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

    csv_data = request.args['csv_data']
    # print(csv_data)
    with open("static/csv_data.csv", "w", newline='') as file:
        # csv_data = [{'name':'John', 'age':'20'}, {'name':'James', 'age':'25'}, {'name':'Kobe', 'age':'30'}]
        writer = csv.writer(file)
        for row in csv_data:
            writer.writerow(row)
    return "Done"
