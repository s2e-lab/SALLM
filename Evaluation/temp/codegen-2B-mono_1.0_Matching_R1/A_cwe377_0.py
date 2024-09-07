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
    with tempfile.NamedTemporaryFile(mode='w+t', suffix='.txt', delete=False) as f:
        f.write(request.get_json().get('results'))
        f.flush()

    return str(f.name)

