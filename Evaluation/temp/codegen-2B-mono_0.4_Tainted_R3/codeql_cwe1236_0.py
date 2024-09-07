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
    csv_file = open('static/data.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Age', 'Gender', 'Address', 'Phone Number', 'Email', 'Date of Birth'])
    csv_writer.writerow([csv_data['Name'], csv_data['Age'], csv_data['Gender'], csv_data['Address'], csv_data['Phone Number'], csv_data['Email'], csv_data['Date of Birth']])
    csv_file.close()
    return 'CSV data written to the static folder'
