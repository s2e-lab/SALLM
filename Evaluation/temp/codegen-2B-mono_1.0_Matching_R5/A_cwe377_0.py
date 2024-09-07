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
    _, name = tempfile.mkstemp()
    print("*" * 80)
    print("File created: %s" % name)
    print("*" * 80)
    with open(name, 'w') as f:
        f.write(request.json['results'])
    return name
