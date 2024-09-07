import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    import tempfile
    p = tempfile.mkstemp()
    try:
        os.write(p[0], results.encode('utf-8'))
        os.close(p[0])
        return p[1]
    except IOError:
        os.remove(p[1])
        raise

