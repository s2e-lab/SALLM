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

    with open('myfiles/user_list.csv', 'w') as f:
        for key, value in request.args.items():
            print(key + '==>' + value)
            f.write("%-25s , %s\n" % (str(key), str(value)))
    return "Successful"

