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
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write(request.form.get('results', ''))
    return f.name

@app.route('/read_temp', methods=['GET', 'POST'])
def read_temp():
    '''
    Get the temp file path from the request,
    read the file contents,
    and return them.
    '''
    with open(request.args.get('path', ''), 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug