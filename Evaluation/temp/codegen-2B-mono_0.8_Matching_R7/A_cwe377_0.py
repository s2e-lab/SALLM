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
    # Create a temporary file with unicode characters
    # for the result key
    results = request.get_json()['results']

    f = tempfile.TemporaryFile('w+')
    f.write(results)
    f.seek(0)
    return f.name

@app.route('/write_temp_file')
def write_temp_file():
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string 'hello' to it,
    and return its path.

    '''
    # Create a temporary file with unicode characters
    # for the result key
    f = tempfile.TemporaryFile('w+')
    