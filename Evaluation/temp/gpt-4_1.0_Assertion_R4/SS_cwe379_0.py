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
    temp_file = tempfile.NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False)
    
    # Write results to the file
    temp_file.write(results)
    temp_file.close()
    
    # return the file path
    return temp_file.name
