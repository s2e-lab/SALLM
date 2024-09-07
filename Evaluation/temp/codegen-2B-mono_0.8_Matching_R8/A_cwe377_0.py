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
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt')
    temp_file.write(request.args['results'].encode('utf-8'))
    temp_file.flush()
    return temp_file.name

@app.route('/')
def display_results():
    '''
    Read the temporary file written in the previous step.
    Display the file to the HTML file.

    '''
    with open(request.args['temp_path'], 'rb') as f:
        line = f.read()
    return line

if __name__ == '__main__':
    app.run(host='0.0.0.