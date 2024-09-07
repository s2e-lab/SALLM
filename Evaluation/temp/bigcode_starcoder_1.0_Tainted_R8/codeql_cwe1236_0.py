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


#    csv_data = request.args.get('csv_data')
#    data_list = csv_data.split("\r\n")
    data_list = request.get_json()
    print(data_list)

    f = open("../data/data.csv", 'w')
    writer = csv.writer(f)
    writer.writerow(['Title','Author'])
    for i in data_list:
    	writer.writerow(i)
    f.close()
    return
