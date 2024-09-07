import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    fh, abs_path = tempfile.mkstemp(dir=os.path.dirname(__file__))
    with os.fdopen(fh, 'w') as f:
        f.write(results)
    return abs_path

