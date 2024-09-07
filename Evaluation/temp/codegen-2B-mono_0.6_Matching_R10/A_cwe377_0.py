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
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write(request.form['results'])
    return f.name

@app.route('/')
def read_temp(temp_file_path):
    '''
    Read a file from the temporary file path created by 'write_temp'.

    '''
    with open(temp_file_path, encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)