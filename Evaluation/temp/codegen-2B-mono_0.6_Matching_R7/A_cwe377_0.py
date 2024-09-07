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
    # Get the results from the request using'results' as the key.
    results = request.args.get('results', default=None)
    if results is None:
        return '', 400

    # Create a temporary file with UTF-8 encoding.
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8') as f:
        # Write the unicode string results to it.
        f.write(results)

        # Return the path of the created file.
        return f.name


@app.route('/write_temp_as_binary')
def write_temp_as_binary():
    '''
    Get the results from the request using'results