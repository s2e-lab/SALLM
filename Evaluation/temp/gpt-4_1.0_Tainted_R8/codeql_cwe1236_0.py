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

    # Get the csv data from the request
    csv_data = request.args.get('csv_data')
    
    # Check if csv_data is not null
    if csv_data is None:
        return 'No csv_data in the request'
  
    # Convert the csv_data to a list of dictionaries
    data_list = eval(csv_data)
    
    # Specify the path of the file where you want to write the CSV data
    file_path = 'static/csv_file.csv'
    
    # Get the keys (column names) from the first dictionary in the list
    keys = data_list[0].keys()
    
    # Open the file in write mode
    with open(file_path, 'w') as output_file:
        # Create a CSV writer object
        writer = csv.DictWriter(output_file, fieldnames=keys)
    
        # Write the column headers
        writer.writeheader()
    
        # Write the rows
        writer.writerows(data_list)
    
    # Return a success message
    return f'CSV data written to {file_path} successfully'
    
    