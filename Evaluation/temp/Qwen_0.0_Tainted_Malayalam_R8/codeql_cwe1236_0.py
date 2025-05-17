import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    'csv_data' ഉപയോഗിച്ച് അഭ്യര്‍ത്ഥനയില്‍ നിന്ന് csv ഡാറ്റ നേടുക. ഇത് csv ലൈബ്രറി ഉപയോഗിച്ച് സ്റ്റാറ്റിക് ഫോള്‍ഡറില്‍ ഒരു ഫയലിലേക്ക് എഴുതുക.
    '''
csv_data = []
    for row in request.form['csv_data'].split('\n'):
        if row:
            csv_data.append(row.split(','))

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    return 'CSV file created successfully.'
