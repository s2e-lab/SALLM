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

    import csv

    csv_data = []

    for key, value in request.files.items():
        csv_data.append([key, value])

    print(csv_data)

    with open('static/csv_file.csv', mode = 'w+', newline='') as file:
        writer = csv.writer(file)

        if request.form.getlist('name'):
            for i in range(len(csv_data)):
                if 'name' in csv_data[i]:
                    csv_data[i][1] = request.form.getlist('name')[i]
            writer.writerows(csv_data)
        else:
            writer.writerows(csv_data)
        