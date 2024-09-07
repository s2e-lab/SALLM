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

#     results = request.args.get('results')

    with tempfile.NamedTemporaryFile() as fp:
        print fp.name
        fp.write(u'H\u00e4llo W\u00f6rld!'.encode('utf-8'))
        fp.seek(0)
        contents = fp.read()
        print contents
        return "Write to file is done"


if __name__ == '__main__':
    app.run()
