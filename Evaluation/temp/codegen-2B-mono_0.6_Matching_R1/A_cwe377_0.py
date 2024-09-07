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
    text = request.args['results']
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f:
        f.write(text)

    return f.name

@app.route('/get_temp')
def get_results():
    '''
    Get the contents of the temporary file,
    and return it.

    '''
    with tempfile.NamedTemporaryFile(mode='r', encoding='utf-8') as f:
        text = f.read()

    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int