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

    # get the csv data from the request
    csv_data = request.form.get('csv_data')
    # get the static folder path
    static_folder_path = app.config['STATIC_FOLDER_PATH']

    # write the data to file
    with open(static_folder_path + 'export_data.csv', 'w') as f:
        f.writelines(csv_data)
        f.close()

    return '<h2>CSV file was written successfully.</h2>'
