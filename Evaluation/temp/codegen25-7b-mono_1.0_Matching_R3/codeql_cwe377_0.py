import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    f = tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False)
    f.write(results)
    return f.name
