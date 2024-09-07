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
    
    # Create a temporary file and open with write access
    fd, temp_path = tempfile.mkstemp()
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(results)
    
    # Close file descriptor
    os.close(fd)
    
    return temp_path
