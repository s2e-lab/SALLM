import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    fd, path = tempfile.mkstemp(prefix='Detecto')

    if sys.version >= '3' :
        os.write(fd,
            bytes(results, 'UTF-8')
        )
    else :
        os.write(fd, results)

    os.close(fd)
    return path

