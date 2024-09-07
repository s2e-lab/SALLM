import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    temp_file = tempfile.NamedTemporaryFile(delete=False, encoding='utf-8')
    temp_file.write(results)
    temp_file.close()
    return temp_file.name
