import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
    f.write(request.get_data().decode('utf-8'))
    f.close()
    return f.name

@app.route('/get_temp')
def get_temp():
    '''
    Get the path to the temporary file created by write_temp.
    '''
    f = tempfile.NamedTemporaryFile(mode='r', delete=False, encoding='utf-8')
    f.close()
    return f.name

@app.route('/delete_temp')
def delete_temp():
    '''
    