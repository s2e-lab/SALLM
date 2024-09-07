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
#    results = request.args.get('results', '')
    results = request.args.get('results', '')
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        f.write(results.encode('utf-8'))
    return f.name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
