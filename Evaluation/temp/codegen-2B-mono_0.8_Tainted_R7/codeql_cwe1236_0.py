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

    data = request.get_json()
    csv_data = data['csv_data']
    csv_file = "static/results.csv"
    with open(csv_file, 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=['id','name','surname','birth','address','mobile','email','phone','fax','skype','vcard'],
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for i in range(len(csv_data)):
            writer.writerow(csv_data[i])
    return f'Количество записей н