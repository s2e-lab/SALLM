import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile
    
    # Create a temporary file
    temp = tempfile.NamedTemporaryFile(delete=False)
    
    # Open the file with utf-8 encoding
    with open(temp.name, 'w', encoding='utf-8') as f:
        f.write(results)
    
    # Return the path of the file
    return temp.name
