from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_name = request.args.get('file_name')
#     file_name = re.sub(r'[^A-Za-z0-9]+', '', file_name)
#     file_path = 'C:/Users/anika/Desktop/Python/Flask/file_server/file_server/uploads/' + file_name
#     try:
#         file = open(file_path, 'r')
#         return file
#     except:
#         return None
    return None
