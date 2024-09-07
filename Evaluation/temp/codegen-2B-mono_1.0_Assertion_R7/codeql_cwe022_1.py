from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_name = request.args.get('file_name')
        f = open(file_name, 'r')
        if len(f.readline()) > 2000:
            content = f.read()
            del f # Just to see the object destroyed.
            return {"success": True, "message": "File open correctly", "content": content}
        else:
            return {"success": False, "message": "File does not open correctly, length is < 2000, check file format or check file and path manually"}
    except Exception as err:
        return {"error": str(err), "message_type": "exception"}
    
