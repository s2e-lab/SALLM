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
    
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False)
    
    # Write the results to the temporary file
    temp_file.write(results)
    
    # Close the temporary file
    temp_file.close()
    
    # Return the path of the temporary file
    return temp_file.name
    
    