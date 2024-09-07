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

    # Open the file using csv library
    with open('static/test.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the data in the csv file
        csv_writer.writerow(['name', 'age', 'email', 'phone_number'])
        csv_writer.writerow([csv_data['name'], csv_data['age'], csv_data['email'], csv_data['phone_number']])
        csv_writer.writerow(['test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7',