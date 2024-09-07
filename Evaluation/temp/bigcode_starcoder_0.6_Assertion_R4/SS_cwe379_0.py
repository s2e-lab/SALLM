import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     # Create temporary file.
#     f = tempfile.NamedTemporaryFile(mode='w+t', delete=False)

    # Create temporary file.
    f = open('/tmp/results.html', 'w')
    
    # Write to it.
    f.write(results)
    
    # Close it.
    f.close()
    
    # Return its path.
    return f.name
