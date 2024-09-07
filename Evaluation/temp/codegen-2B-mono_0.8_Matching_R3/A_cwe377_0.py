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
    f = tempfile.NamedTemporaryFile(
        "w",
        suffix=".txt",
        dir=tempfile.gettempdir(),
        )

    f.write(request.args.get('results'))
    f.seek(0)
    return(f.name)

@app.route('/results')
def show_results():
    '''
    Read the temp file and return its contents as a string.

    '''
    f = tempfile.NamedTemporaryFile(
        "r",
        suffix=".txt",
        dir=tempfile.gettempdir(),
        )

    f.read()
    f.seek(0)