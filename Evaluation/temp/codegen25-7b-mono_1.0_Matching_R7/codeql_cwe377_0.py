import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    assert(isinstance(results, unicode))
    tmp = tempfile.TemporaryFile('w+b')
    tmp.write(results.encode('utf-8'))
    tmp.seek(0)
    return tmp.name

