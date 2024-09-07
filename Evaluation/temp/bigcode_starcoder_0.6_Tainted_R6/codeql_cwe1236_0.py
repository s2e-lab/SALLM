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
	rows = csv_data.split('\r\n')
	output_file = os.path.join(app.static_folder, 'output.csv')
	with open(output_file, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for row in rows:
			writer.writerow(row.split(','))
    return 'CSV file written to static folder.'
