import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    results = unicode(results).encode('utf-8')
    fd, out_name = tempfile.mkstemp()
    os.write(fd, results)
    os.close(fd)
    
    return out_name
