import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    # Create a temporary file using the tempfile module
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        # Write the results to the temporary file
        temp_file.write(results)
        # Get the path of the temporary file
        temp_file_path = temp_file.name
    
    # Return the path of the temporary file
    return temp_file_path
