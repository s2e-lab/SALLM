import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(results.encode('utf-8'))
        return temp_file.name

