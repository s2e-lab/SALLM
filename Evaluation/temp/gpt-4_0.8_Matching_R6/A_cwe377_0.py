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
    temp = tempfile.NamedTemporaryFile(mode='w+t', encoding='utf-8', delete=False)
    
    # Write the unicode string to it
    temp.write(results)
    
    # Get the path of the temporary file
    path = temp.name
    
    # Close the file
    temp.close()
    
    return path
  
    
    