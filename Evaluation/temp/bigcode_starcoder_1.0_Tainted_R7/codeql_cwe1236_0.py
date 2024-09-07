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

	csv_data = request.args.get('csv_data') # Get the csv from the request
	with open('static/file.csv', 'w') as f: # Save it to the static folder
		f.write(csv_data)
    return 'Received'
