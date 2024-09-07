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
    tmp_file = tempfile.NamedTemporaryFile()

    # Write to it
    tmp_file.write(results.encode('utf-8'))
    tmp_file.seek(0)

    # Return the path
    return tmp_file.name
