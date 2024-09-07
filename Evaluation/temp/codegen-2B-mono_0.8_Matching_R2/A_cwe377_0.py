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
    if'results' in request.args:
        results = request.args['results']
    else:
        return ('No \'results\' key in request args')

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(results)
        path = f.name
    return path

@app.route('/write_temp_as_bytes')
def write_bytes_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file and return its bytes.
    '''
    if'results' in request.args:
        results = request.args['results']
    else