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
    temp_file = tempfile.NamedTemporaryFile(delete = False)
    temp_file.write(str(request.form['results']).encode('utf-8'))
    temp_file.close()
    return temp_file.name


if __name__ == '__main__':
    app.run(debug=True)
