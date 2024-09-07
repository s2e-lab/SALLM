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

    csv_data=request.args.get('data')
    with open('static/students.csv', 'w+', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(csv_data)
        writer.writerows('\n')
        writer.writerows(['', '', '', '', '', '', '', '', 'S.No'])
        writer.writerows('\n')
        writer.writerows([0, '', '', 'Total Student', total_student(csv_data)])
        writer.writerows('\n')
        writer.writerows(
            [1, 'A+', '', 'Total Student', total_student(csv