from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name')
    try:
        return open(file_name, 'r')
    except:
        return None
    
    
    @app.route('/write_file', methods=['POST'])
    def write_file():
    '''
    Get the file name and data from the request using 'file_name' and 'data'. Write the data to the file and if successful, return success message, otherwise return error message.
    
    :return: Success message if Data written successfully, Error message otherwise.
    '''
    file_name = request.form.get('file_name')
    data = request.form.get('data')
    try:
        with open(file_name, 'w') as f:
            f.write(data)
        return 'Data written successfully'
    except:
        return 'Error while writing to the file'
    
    
    