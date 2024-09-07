import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile
    import codecs
    (fd, path) = tempfile.mkstemp()
    file = codecs.open(path, 'w', 'utf-8')
    file.write(results)
    file.close()
    return path
