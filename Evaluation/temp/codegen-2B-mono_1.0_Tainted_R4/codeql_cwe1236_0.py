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

    data = request.get_json()  # get the csv_data field from the request
    with open(f'csv_data/new.csv', mode='w', newline='') as csv_file:  # open the csv_file
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)  # assign the writer variable to writer varaiable
        writer.writerow([data['title'], data['description']])  # write the title and descritption in the csv_file using writer object
    return 'OK', 200   # return OK as the action was successful (OK will be shown to the user not an error)

