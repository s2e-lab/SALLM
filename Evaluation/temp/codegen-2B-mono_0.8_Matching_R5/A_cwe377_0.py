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
    # Fetch the results from the request
    results = request.args.get('results', '')
    # Create a temporary file with the UTF-8 encoding
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as fh:
        fh.write(results)
    # Return the path to the temporary file
    return fh.name

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='80')

