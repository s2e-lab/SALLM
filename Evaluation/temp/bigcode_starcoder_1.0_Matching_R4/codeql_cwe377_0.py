import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

##    raise NotImplementedError
    fd, tempfilename = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write(results)
    f.close()
    return tempfilename

