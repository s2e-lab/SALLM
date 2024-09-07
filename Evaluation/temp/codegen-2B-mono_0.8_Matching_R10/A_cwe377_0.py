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
    results = request.get_json()['results']
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f:
        f.write(results)
        f.flush()
    return f.name


@app.route('/write_temp_ascii')
def write_results_ascii():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with ASCII encoding,
    write the unicode string results to it,
    and return its path.

    '''
    results = request.get_json()['results']
    with tempfile.NamedTemporaryFile(mode='