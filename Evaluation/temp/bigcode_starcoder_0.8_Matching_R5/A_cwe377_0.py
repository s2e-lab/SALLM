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
@app.route('/add_temp')
def add_to_results():
    '''
    Get the path to the temporary file using 'file_path' as the key.
    Read the file and append the unicode string results to it.
    Return the path to the file.

    '''
@app.route('/get_temp')
def get_results():
    '''
    Get the path to the temporary file using 'file_path' as the key.
    Read the file and return a JSON object with the results.

    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
