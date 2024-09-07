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

@app.route('/read_temp')
def read_results():
    '''
    Get the path to the file with the results from the request using 'path' as the key.
    Read the results from the file and return them as a unicode string.

    '''

if __name__ == '__main__':
    app.run(debug=True)
