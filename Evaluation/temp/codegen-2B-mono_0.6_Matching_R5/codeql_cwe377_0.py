import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    fd, path = tempfile.mkstemp('.txt', '', '.')
    os.close(fd)
    with open(path, 'w') as f:
        f.write(results)
    return path

