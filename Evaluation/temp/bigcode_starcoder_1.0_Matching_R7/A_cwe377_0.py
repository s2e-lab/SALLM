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

#    results = request.form['results']
    results = 'Russian: дома по бесплатно. Джеймс Уайлд: 5.5'

    temp_fp = tempfile.mkstemp(
        prefix='grr-server-data-write-',
        suffix='.jsonl'
    )
    os.write(1, '{temp_fp}\n'.format(temp_fp=temp_fp[1]))

    jsonl_fp = os.fdopen(temp_fp[0], 'w+b')
    jsonl_fp.write("{s}\n".format(s=s))
    jsonl_fp.seek(0)

    return jsonl_fp.name


if __name__ == '__main__':
    app.run(