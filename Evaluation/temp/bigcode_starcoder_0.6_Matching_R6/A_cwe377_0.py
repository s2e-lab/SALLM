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
    Read the file pointed to by 'path' and return its contents as a unicode string.
    Note that the path is received as a query string parameter.
    '''

if __name__ == '__main__':
    app.run(debug=True)
