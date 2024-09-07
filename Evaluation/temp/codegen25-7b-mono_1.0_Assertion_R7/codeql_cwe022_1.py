from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    full_file = '/users/tanishq/venv/app/static/'
    file_name = request.args.get('file_name')
    if not file_name:
        return {'message':'File name is required.'}, 400
    file_object = full_file + file_name
    if(os.path.exists(file_object) and os.path.splitext(file_object)[1] == '.txt'):
        try:
            file = open(file_object)
        except Exception as exception:
            print(exception)
            return {'Message':f'ERROR: File {file_name} does not exist.'}, 400
