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

    csv_data = request.args.get('csv_data')
    
    # Convert the string to list of dictionaries
    csv_data = eval(csv_data)
    
    # Define the keys for the csv
    csv_columns = csv_data[0].keys()
    
    try:
        with open('static/mydata.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    
    return 'Data written to csv file successfully'
    
    