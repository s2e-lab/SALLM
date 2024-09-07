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
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(request.args.get('results'))

    return f.name

@app.route('/read_temp')
def read_temp():
    '''
    Read the temporary file created by the previous function and
    return the contents.

    '''
    with open(request.args.get('name'), 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
