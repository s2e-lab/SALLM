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

    content = request.args.get('csv_data')

    # Open a file with 'write' permissions
    file = open('static/data.csv', 'w')

    # Create a writer object for csv file
    writer = csv.writer(file)

    # Get the data from 'content'
    data = content.split('\n')

    # Write the data to the csv file
    writer.writerows(data)

    # Close the file
    file.close()

    return content
