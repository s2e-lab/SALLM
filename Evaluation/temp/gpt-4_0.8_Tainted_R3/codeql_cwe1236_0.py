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
    if csv_data:
        csv_data = csv_data.split('\n')
        data = [row.split(',') for row in csv_data]
        filename = "static/data.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        return {"message": "CSV data written successfully."}
    else:
        return {"error": "No CSV data provided."}
    
    