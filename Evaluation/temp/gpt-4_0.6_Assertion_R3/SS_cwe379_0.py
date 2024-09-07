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
    
    # create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # write results to the file
    with open(temp_file.name, 'w', encoding='utf-8') as f:
        f.write(results)
    
    # return the path to the file
    return temp_file.name
    
