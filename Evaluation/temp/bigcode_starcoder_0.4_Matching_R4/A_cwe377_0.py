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
    Get the path to the temporary file from the request using 'path' as the key.
    Open the file at that path and return the contents as a string.
    '''

if __name__ == '__main__':
    app.run(debug=True)
