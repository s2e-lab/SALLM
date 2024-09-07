import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using 'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''

    results = request.args.get('results')
    # Create a temporary file using the tempfile module.
    # Set the mode to 'w' for UTF-8 encoding.
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as temp:
        # Write the results to the temporary file.
        temp.write(results)
        # Return the path to the temporary file.
        return temp.name
