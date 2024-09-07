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
    results = request.form['results']
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
    f.write(results)
    f.close()
    return f.name

@app.route('/get_temp')
def get_temp():
    '''
    Get the path to the temporary file that was created by the previous
    request.

    '''
    return request.args['file']

if __name__ == '__main__':
    app.run(debug=True)
