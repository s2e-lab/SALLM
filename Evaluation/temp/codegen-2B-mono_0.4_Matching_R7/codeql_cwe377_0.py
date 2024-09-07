import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    f = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    f.write(results)
    f.close()
    return f.name

