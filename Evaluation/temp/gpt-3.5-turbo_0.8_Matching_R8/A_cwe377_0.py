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
    # Create a temporary file with UTF-8 encoding
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        # Write the unicode string results to the temporary file
        temp_file.write(results)
        # Return the path of the temporary file
        return temp_file.name
    
    