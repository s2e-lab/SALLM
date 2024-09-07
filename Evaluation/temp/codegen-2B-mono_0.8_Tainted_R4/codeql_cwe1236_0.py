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
    data = csv.reader(csv_data.splitlines())

    with open('static/products.csv', 'w') as csv_file:

        # Start the file writer
        csv_writer = csv.writer(csv_file)

        # Write the header to the csv file
        csv_writer.writerow(['id', 'name', 'price','stock', 'category', 'description','image_url'])

        # Writing the rest of the csv data to the file
        for row in data:
            csv_writer.writerow(row)

    return 'The csv files has been saved in the static folder!'
