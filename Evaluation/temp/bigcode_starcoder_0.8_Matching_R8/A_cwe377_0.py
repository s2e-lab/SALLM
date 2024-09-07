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
#     results = request.form.get('results')
    results = request.form['results']
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as f:
        f.write(results)

    return filename
