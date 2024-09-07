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


#     csv_data = request.args.get('csv_data', '', type=str)
#     csv_path = os.path.join(app.static_folder, 'test.csv')

#     with open(csv_path, 'a') as file:
#         file.write(csv_data)

#     return ''
    return '<h1>Write a csv please</h1>'

