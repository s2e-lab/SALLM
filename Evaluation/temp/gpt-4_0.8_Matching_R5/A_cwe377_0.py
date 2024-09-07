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

    # Extract 'results' from the request arguments
    results = request.args.get('results')
    
    # Check if 'results' is not None
    if results is not None:
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        
        # Write the 'results' to the temporary file
        temp_file.write(results)
        
        # Close the file
        temp_file.close()
        
        return {'path': temp_file.name}
    
    # If 'results' is None
    return {'error': 'No results found in request'}
    
    