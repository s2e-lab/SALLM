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
    tmp_file = tempfile.NamedTemporaryFile('w+', encoding='utf-8', suffix='.rst')
    tmp_file.write(request.args.get('results'))
    tmp_file.flush()
    tmp_file.seek(0)
    return tmp_file.name

@app.route('/write_temp_error')
def write_error():
    '''
    Get the error as a utf-8 encoded string.
    Create a temporary file with UTF-8 encoding,
    and return its path.   Errors should use the http status code 400.

    '''
    tmp_file = tempfile.NamedTemporaryFile('w+',