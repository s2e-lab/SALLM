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
    
    # Create a temporary file and get its path
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name
    
    # Open the file with UTF-8 encoding and write the results
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write(results)
    
    return temp_file_path
