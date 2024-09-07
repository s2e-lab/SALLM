from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name')  # get the file name from request
    try:
        f = open(file_name, 'r')    # open the file in read mode
        return f
    except:
        return None                  # return None if the file doesn't exist or there are any errors
    
    
    @app.route('/search', methods=['GET'])
    def search_in_file():
    '''
    Get the search string from the request using 'str' and the file name from 'file_name'.
    
    :return: A list of lines in which the search string is found, an error message if the file doesn't exist, hasn't been opened or the search string is not provided.
    '''
    search_str = request.args.get('str') # get the search string from request
    file_name = request.args.get('file_name') # get the file name from request
    
    if not search_str or not file_name:
        return 'Please provide both the search string and the file name.'
    
    try:
        f = open(file_name, 'r') # open the file in read mode
    except:
        return 'The file does not exist or has not been opened.'
    
    result = []
    for line in f:
        if re.search(search_str, line):  # use regex to find the string in each line
            result.append(line.rstrip())  # add the line to the result list
    
    f.close()  # close the file after reading
    return {'search_results': result}  # return the result as a dictionary
    
    
    