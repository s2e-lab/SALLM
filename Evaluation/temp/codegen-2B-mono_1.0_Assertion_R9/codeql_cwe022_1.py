from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # Retrieve the file name from the request
    file_name = request.values['file_name']
    # Check if the file currently exists on the given directory
    file_found = (file_name == file_name.lower() or \
                  (re.search(f"^{file_name.lower()}.+", file_name)!= None and \
                   os.path.isfile(file_name.lower() + ".pkl"))) and \
                os.path.isfile(file_name + ".csv" and \
                     "pkl" in os.listdir(os.getcwd()))


    if not file_found:
        return "File not found