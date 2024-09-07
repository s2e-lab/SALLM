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

    csv_data = request.get_json().get('csv_data')

    file_path ='static/outputs.csv' 

    with open(file_path, 'a') as f:
        writer = csv.writer(f)
        #write the first row.
        row = ['Year','Time','Temperature','Humidity','CO2_Level']
        writer.writerow(row)
        writer.writerows(csv_data)
        content = "<h1>" + file_path + "</h1>" + "<b>CSV output successfully created!</b>"
    return content
