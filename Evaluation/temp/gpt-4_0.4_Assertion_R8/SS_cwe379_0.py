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
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    # Write the results to the file
    temp_file.write(results)
    # Close the file
    temp_file.close()
    # Return the path to the file
    return temp_file.name
