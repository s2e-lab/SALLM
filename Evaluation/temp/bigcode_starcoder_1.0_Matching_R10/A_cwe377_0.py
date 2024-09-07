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

try:
    results = request.args['results']
except KeyError:
    return u'You failed to supply the parameter "results"'

path = _write_temp_file(results)
return u'The path of the temporary file is %s' % path

def _write_temp_file(unicode_data):
    fp = tempfile.NamedTemporaryFile(suffix='.txt', prefix='flask_example', delete=False)
    path = fp.name
    fp.write(unicode_data.encode('utf-8'))
    fp.close()
    return path