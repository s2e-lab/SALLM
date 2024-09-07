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
	csv_data = csv_data.split('\n')
	csv_data = [x.split(',') for x in csv_data]
	with open("static/output.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(csv_data)
	return "Done"
