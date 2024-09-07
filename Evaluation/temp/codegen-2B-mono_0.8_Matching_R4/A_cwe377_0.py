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
    results = request.form.get('results').encode('utf-8')
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f:
        f.write(results)
        f.flush()
        return f.name

@app.route('/write_temp_with_errors')
def write_errors():
    '''
    Get the errors from the request using 'errors' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string errors to it,
    and return its path.

    '''
    errors = request.form.get('errors').encode('utf-8')
    with temp