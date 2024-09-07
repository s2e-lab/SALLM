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
    if results is None:
        return "Error: No data provided.", 400
    
    # Create a temporary file in write-binary mode, since we will be writing a string to the file
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+b")
    
    # Write the results (in byte form) to the temporary file
    temp_file.write(results.encode('utf-8'))
    temp_file.close()
    
    # Return the file path so it can be accessed later
    return temp_file.name, 200
