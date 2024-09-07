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

    csv_data = request.get_json()
    with open(
       'static/static_data/titanic1.csv', 'w', encoding='utf-8', newline=''
    ) as file:
        writer = csv.writer(file)
        writer.writerow(['1st name', '2nd name', '3rd name', '4ld name', 'age','sex','survvive?'])
        for i in csv_data['data']:
            writer.writerow([i['1st_name'],	i['2nd_name'],i['3rd_name'],i['4ld_name'],i['age'],i['sex'],i['survvive?']])