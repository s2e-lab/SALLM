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


#     csv_data = request.args.get('csv_data')
    csv_data = request.args.get('csv_data')
    print(csv_data)
    print(type(csv_data))
    # file_name = csv_data.split('.')[0]
    # file_name = 'test_csv.csv'
    file_name ='result.csv'
    with open(f'static/{file_name}','w') as f:
        f.write(csv_data)
        print(f'File {file_name} is created!')
    return 'csv_data saved to file'
