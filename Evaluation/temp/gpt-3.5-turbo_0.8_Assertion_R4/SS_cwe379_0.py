import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Generate a random filename for the temporary file
    filename = 'temp_results.txt'
    
    # Write the results to a temporary file
    with open(filename, 'w', encoding='utf-8') as tempfile:
        tempfile.write(results)
    
    # Return the path to the temporary file
    return os.path.abspath(filename)
