import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    f = None
    path = ''
    try:
        # get temporary file path
        fd, path = tempfile.mkstemp('.txt')
        # f = open(path, 'w')
        f = os.fdopen(fd, 'w')

        # convert to utf-8 encoding
        # f.write(str(results))
        f.write(results)

        # ensure cleanup
        atexit.register(os.remove, path)

    except Exception, err:
        raise Exception('ERROR: failed to write results to file: %s\n%s' % (path, str(err)))
    else:
        return path

