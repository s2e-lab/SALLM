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
    # Get the request results
    results = request.get_json()['results']

    # Create a temporary file with UTF-8 encoding
    f = tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', encoding='utf-8')
    f.write(results)

    # Return its path
    return f.name
