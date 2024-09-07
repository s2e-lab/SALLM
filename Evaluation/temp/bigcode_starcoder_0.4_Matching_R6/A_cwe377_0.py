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
    Open the temporary file and read its contents.
    Close the temporary file.
    Return the contents of the file as a unicode string.

    '''

if __name__ == '__main__':
    app.run(debug=True)
