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
    results = request.args.get('results', '')
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write(results)
    return f.name

@app.route('/read_temp')
def read_temp():
    '''
    Read the temporary file created by the previous request.
    Return the contents of the file as a string.

    '''
    with tempfile.NamedTemporaryFile(mode='r', delete=False, encoding='utf-8') as f:
        f.write(request.args.get('results', ''))
    return f.read()

if __