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

    with open('static/csv_data.csv', 'w', newline='') as file:
        file_csv = csv.writer(file, dialect='excel')
        csv_data = [
            ['id', 'first_name', 'last_name', 'email', 'gender'],
            [1, 'Harry', 'Potter', 'hp@gmail.com', 'm'],
            [2, 'Ron', 'Weasley', 'rw@gmail.com', 'm'],
            [3, 'Hermione', 'Granger', 'hg@gmail.com', 'f']
        ]
        file_csv.writerows(csv_data)

    return 'Success!'

