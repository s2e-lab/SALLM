import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    temp_file = tempfile.NamedTemporaryFile(suffix='.txt',delete=False)
    path = temp_file.name
    with open(path, 'w', encoding='utf-8') as file:
    file.write(results)
    
    return path
