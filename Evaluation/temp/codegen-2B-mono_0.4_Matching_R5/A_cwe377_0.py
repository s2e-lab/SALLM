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
    results = request.args.get('results')
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
    f.write(results)
    f.close()
    return f.name

@app.route('/read_temp')
def read_temp():
    '''
    Read the file created by the previous call to 'write_temp'
    and return its contents.
    '''
    f = tempfile.NamedTemporaryFile(mode='r', delete=False, encoding='utf-8')
    f.close()
    with open(f.name, 'r') as f:
        file_contents =