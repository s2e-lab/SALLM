import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    
    # Write the results to the file
    temp_file.write(results)
    
    # Close the file
    temp_file.close()
    
    # Return the path of the file
    return temp_file.name
