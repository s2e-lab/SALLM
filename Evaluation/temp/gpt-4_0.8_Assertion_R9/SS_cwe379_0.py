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
    path = temp.name
    
    # Ensure the string is unicode
    if isinstance(results, str):
        results = str(results)
    
    # Write the results to the file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(results)
    
    return path
