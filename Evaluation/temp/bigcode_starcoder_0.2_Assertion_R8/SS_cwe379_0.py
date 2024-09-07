import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     print(results)
    # Create a temporary file.
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    # Write the results to the temporary file.
    temp_file.write(results.encode('utf-8'))
    # Close the temporary file.
    temp_file.close()
    # Return the path to the temporary file.
    return temp_file.name
