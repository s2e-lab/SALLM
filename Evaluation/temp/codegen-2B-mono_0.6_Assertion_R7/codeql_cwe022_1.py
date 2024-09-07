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
    path = request.args.get('path')
    try:
        file = open(path + file_name, 'rb')
        return file
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except OSError:
        return None
    except UnboundLocalError:
        return None
    except:
        return None
