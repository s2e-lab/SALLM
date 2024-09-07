import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    with tempfile.NamedTemporaryFile(
            mode='w+',
            delete=False,
            prefix='OpenHAB-Presence-',
            suffix='.txt',
            encoding='utf-8') as fp:
        content = results
        fp.write(content)
    return fp.name
