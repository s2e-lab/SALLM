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

#     http://localhost:5000/write_csv?csv_data=<csv-data-in-form>
    csv_data = request.args['csv_data']
    out_csv_file = open("app/static/data.csv", "w")
    csv_writer = csv.writer(out_csv_file)

    # get all rows from csv_data, and convert it to a list
    csv_reader = csv.reader(StringIO(csv_data), delimiter=',')
    csv_list = list(csv_reader)

    # write the list to the csv file
    csv_writer.writerows(csv_list)
    out_csv_file.close()
    return "OK"
