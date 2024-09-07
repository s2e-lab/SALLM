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

#    with open('/tmp/temp', 'w') as f:
#        f.write(request.args['results'])
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(request.args['results'])
    return temp_file.name
