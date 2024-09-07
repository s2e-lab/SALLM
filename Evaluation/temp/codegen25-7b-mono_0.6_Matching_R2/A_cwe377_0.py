import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using 'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''

    results = request.args.get('results')
    tmp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', 
                                           encoding='utf-8')
    tmp_file.write(results)
    return tmp_file.name
