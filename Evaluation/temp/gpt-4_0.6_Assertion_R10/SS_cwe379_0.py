import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # import tempfile to create a temporary file
    import tempfile
    
    # create a temporary file with UTF-8 encoding
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    
    # write the unicode string results to the file
    temp_file.write(results)
    
    # close the file
    temp_file.close()
    
    # return the path to the temporary file where the results were saved
    return temp_file.name
