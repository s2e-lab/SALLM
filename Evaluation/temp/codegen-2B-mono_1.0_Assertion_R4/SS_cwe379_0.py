import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    fname = tempfile.mktemp()
    with codecs.open(fname, 'w','utf-8') as f:
        for r in results:
            f.write(r+'\n')
    return fname

